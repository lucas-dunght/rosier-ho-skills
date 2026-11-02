#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-exec-task-dispatch-auto:
Điều Phối Giao Việc Tự Động 3 Phân Hệ (Todolist · Kế Hoạch · Quy Trình) Kèm Cổng Hỏi Lại Khử Mơ Hồ
Part of Rosier Master Skill Ecosystem (RS-OS 200 · Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    CLOSED_STORES,
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
    sanitize_rosier_text,
)

SKILL_ID = "rs-exec-task-dispatch-auto"
DIVISION_CODE = "01"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"

DATE_RE = re.compile(r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{4})\b")
TIME_RE = re.compile(r"\b(\d{1,2}:\d{2})\b")


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_exec_task_dispatch_auto_tool.py]",
        "skill_id": SKILL_ID,
        "dry_run": dry_run,
        "error": {
            "code": code,
            "root_cause": root_cause,
            "next_command": next_command,
        },
    }, ensure_ascii=False, indent=2))
    return 1


def _norm_date(raw: str) -> str:
    s = raw.strip().replace("-", "/")
    parts = s.split("/")
    if len(parts) == 3:
        return f"{int(parts[0]):02d}/{int(parts[1]):02d}/{parts[2]}"
    return s


def _extract_quoted_or_after(text: str, markers: Tuple[str, ...], stop_words: Tuple[str, ...]) -> str:
    low = text.lower()
    for mk in markers:
        idx = low.find(mk)
        if idx != -1:
            after = text[idx + len(mk):].strip(" :,-")
            q_match = re.match(r'^["\']([^"\']+)["\']', after)
            if q_match:
                return q_match.group(1).strip()
            cut = len(after)
            after_low = after.lower()
            for sw in stop_words:
                s_idx = after_low.find(sw)
                if s_idx != -1 and s_idx < cut:
                    cut = s_idx
            candidate = after[:cut].strip(" .,;:-")
            if candidate:
                return candidate
    return ""


def _extract_assignees(text: str, explicit_assignees: str) -> List[str]:
    if explicit_assignees:
        return [x.strip() for x in explicit_assignees.split(",") if x.strip()]
    low = text.lower()
    if any(k in low for k in ("cho chính mình", "cho tôi", "tự làm", "của tôi")):
        return ["SELF"]
    stop_markers = (
        " vào ngày", " ngày ", " từ ngày", " từ ", " đến ", " trong nhóm",
        " thuộc kế hoạch", " của kế hoạch", " theo quy trình", " độ ưu tiên",
        " mức ưu tiên", " lúc ", " trước ", " hạn chót",
    )
    extracted = _extract_quoted_or_after(text, ("giao cho ", "phân công cho ", " cho "), stop_markers)
    if extracted and len(extracted) <= 80:
        bad_prefixes = ("kế hoạch", "quy trình", "nhóm công việc", "mẫu", "nhóm mẫu", "công việc", "việc")
        if not any(extracted.lower().startswith(bp) for bp in bad_prefixes):
            return [x.strip() for x in re.split(r"\s+và\s+|,", extracted) if x.strip()]
    return []


def _extract_task_title(text: str, explicit_title: str) -> str:
    if explicit_title.strip():
        return explicit_title.strip()
    q_match = re.search(r'["\']([^"\']{3,150})["\']', text)
    if q_match:
        return q_match.group(1).strip()
    stop_markers = (
        " trong nhóm công việc", " vào nhóm công việc", " thuộc kế hoạch", " của kế hoạch",
        " trong kế hoạch", " theo quy trình", " từ quy trình", " cho ", " vào ngày",
        " ngày ", " từ ngày", " từ ", " đến ngày", " hôm nay", " ngày mai",
    )
    prefixes = (
        "tạo công việc chính ", "tạo công việc phụ ", "tạo công việc ", "giao công việc ",
        "giao việc todolist ", "giao việc ", "tạo nhiệm vụ ", "giao nhiệm vụ ",
        "áp nhóm mẫu ", "giao nhóm mẫu ", "giao theo mẫu ",
    )
    extracted = _extract_quoted_or_after(text, prefixes, stop_markers)
    return extracted


def classify_task_dispatch(payload: Dict[str, Any], dry_run: bool = False) -> Dict[str, Any]:
    """
    Deterministic 4-Gate Task Dispatch Classifier & Ambiguity Detector:
      - Gate 1: Channel Selection (TODOLIST vs WORK_PLAN vs WORKFLOW_MISSION)
      - Gate 2: Target Container (Template/Group vs Plan/Group vs Workflow)
      - Gate 3: Assignee Resolution (Staff Name/Role or SELF or Workflow Step-1 Default)
      - Gate 4: Task Title & Time Window (Single Date + HH:mm vs Start Date + End Date)
    """
    raw_query = str(payload.get("query") or payload.get("text") or "").strip()
    sanitized_query = sanitize_rosier_text(raw_query)
    low_q = sanitized_query.lower()

    explicit_store = str(payload.get("store_code") or "").strip()
    for c_code in CLOSED_STORES:
        if c_code == explicit_store or c_code in low_q or c_code in raw_query.lower():
            return {
                "ok": False,
                "status": "BLOCKED",
                "claim_label": "[OBSERVED: core/rs_core_engine.py]",
                "skill_id": SKILL_ID,
                "route_blocked": True,
                "blocked_store_code": c_code,
                "reason": f"Điểm bán {c_code} ({CLOSED_STORES[c_code]}) đã ngừng hoạt động vĩnh viễn theo khóa ngữ cảnh Rosier.",
                "next_command": "python3 .agent/skills/rs-exec-task-dispatch-auto/scripts/rs_exec_task_dispatch_auto_tool.py --self-test --json",
            }

    confirmed = bool(payload.get("confirmed", False))
    explicit_channel = str(payload.get("channel") or "").upper().strip()
    if explicit_channel == "WORKFLOW":
        explicit_channel = "WORKFLOW_MISSION"
    explicit_submode = str(payload.get("submode") or "").lower().strip()

    dates_found = [_norm_date(d) for d in DATE_RE.findall(sanitized_query)]
    times_found = TIME_RE.findall(sanitized_query)

    explicit_date = _norm_date(str(payload.get("date") or "")) if payload.get("date") else ""
    explicit_start_time = str(payload.get("start_time") or "").strip()
    explicit_end_time = str(payload.get("end_time") or "").strip()
    explicit_date_start = _norm_date(str(payload.get("date_start") or "")) if payload.get("date_start") else ""
    explicit_date_end = _norm_date(str(payload.get("date_end") or "")) if payload.get("date_end") else ""

    has_single_day_word = any(w in low_q for w in ("hôm nay", "ngày mai", "sáng nay", "chiều nay", "tối nay", "ca sáng", "ca chiều", "ca tối"))
    has_range_word = any(w in low_q for w in ("từ ngày", "đến ngày", "trong tuần", "tuần này", "tháng này", "sprint"))

    # 1. Score 3 Channels
    todo_signals: List[str] = []
    plan_signals: List[str] = []
    workflow_signals: List[str] = []

    for kw in ("todolist", "to-do", "việc trong ngày", "theo mẫu", "từ mẫu", "nhóm mẫu", "gói mẫu", "bộ mẫu", "mẫu công việc", "checklist", "ca sáng", "ca chiều", "ca tối"):
        if kw in low_q:
            todo_signals.append(kw)
    if (len(dates_found) == 1 or has_single_day_word) and len(times_found) >= 1 and not has_range_word:
        todo_signals.append("single_date_with_hours")

    for kw in ("kế hoạch", "nhóm công việc", "công việc chính", "cvc", "công việc phụ", "cvp", "sheet", "dự án", "chiến dịch", "story point"):
        if kw in low_q:
            plan_signals.append(kw)
    if (len(dates_found) >= 2 or has_range_word) and "quy trình" not in low_q:
        plan_signals.append("multi_day_range")

    for kw in ("quy trình", "nhiệm vụ quy trình", "luồng duyệt", "chuyển tiếp nhiệm vụ", "bàn giao bước", "tạo nhiệm vụ"):
        if kw in low_q:
            workflow_signals.append(kw)

    resolved_channel = ""
    if explicit_channel in ("TODOLIST", "WORK_PLAN", "WORKFLOW_MISSION"):
        resolved_channel = explicit_channel
    else:
        scores = {
            "WORKFLOW_MISSION": len(workflow_signals) * 30,
            "WORK_PLAN": len(plan_signals) * 25,
            "TODOLIST": len(todo_signals) * 25,
        }
        max_channel = max(scores, key=lambda k: scores[k])
        max_val = scores[max_channel]
        non_zero = [k for k, v in scores.items() if v > 0]
        if max_val > 0 and len(non_zero) == 1:
            resolved_channel = max_channel
        elif max_val > 0 and len(non_zero) > 1:
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            if sorted_scores[0][1] > sorted_scores[1][1]:
                resolved_channel = sorted_scores[0][0]

    gate_1_channel_clear = bool(resolved_channel)

    # 2. Extract Container / Template / Submode
    plan_keyword = str(payload.get("plan_keyword") or "").strip() or _extract_quoted_or_after(
        sanitized_query,
        ("thuộc kế hoạch ", "của kế hoạch ", "trong kế hoạch ", "kế hoạch "),
        (" nhóm công việc", " cho ", " từ ngày", " ngày ", " đến ngày", " độ ưu tiên"),
    )
    group_keyword = str(payload.get("group_keyword") or "").strip() or _extract_quoted_or_after(
        sanitized_query,
        ("trong nhóm công việc ", "vào nhóm công việc ", "nhóm công việc "),
        (" của kế hoạch", " thuộc kế hoạch", " trong kế hoạch", " cho ", " từ ngày", " ngày ", " đến ngày"),
    )
    parent_task_keyword = str(payload.get("parent_task_keyword") or "").strip() or _extract_quoted_or_after(
        sanitized_query,
        ("dưới công việc chính ", "dưới công việc ", "thuộc công việc chính "),
        (" trong kế hoạch", " của kế hoạch", " cho ", " từ ngày", " ngày "),
    )
    workflow_keyword = str(payload.get("workflow_keyword") or "").strip() or _extract_quoted_or_after(
        sanitized_query,
        ("theo quy trình ", "từ quy trình ", "trong quy trình ", "quy trình "),
        (" cho ", " từ ngày", " ngày ", " đến ngày", " bắt đầu"),
    )
    template_keyword = str(payload.get("template_keyword") or "").strip() or _extract_quoted_or_after(
        sanitized_query,
        ("nhóm mẫu ", "gói mẫu ", "theo mẫu ", "từ mẫu ", "mẫu công việc "),
        (" cho ", " vào ngày", " ngày ", " hôm nay", " ngày mai", " từ "),
    )

    submode = explicit_submode
    target_mcp_tool = ""
    pre_lookup_tools: List[str] = []

    if resolved_channel == "TODOLIST":
        if not submode:
            if any(k in low_q for k in ("nhóm mẫu", "gói mẫu", "bộ mẫu", "áp nhóm")):
                submode = "template_group"
            elif any(k in low_q for k in ("theo mẫu", "từ mẫu", "mẫu công việc")):
                submode = "template"
            else:
                submode = "adhoc"
        if submode == "template_group":
            target_mcp_tool = "todo_template_apply_group"
            pre_lookup_tools = ["todo_template_list_groups", "members_search"]
        elif submode == "template":
            target_mcp_tool = "todo_create_from_template"
            pre_lookup_tools = ["todolist_list_templates", "members_search"]
        else:
            target_mcp_tool = "todo_create"
            pre_lookup_tools = ["members_search"]
    elif resolved_channel == "WORK_PLAN":
        if not submode:
            if any(k in low_q for k in ("công việc phụ", "cvp", "việc phụ")):
                submode = "subtask"
            elif any(k in low_q for k in ("tạo sheet", "sheet mới")):
                submode = "sheet_bundle"
            else:
                submode = "main_task"
        if submode == "subtask":
            target_mcp_tool = "work_plan_subtask_create"
            pre_lookup_tools = ["work_plan_list", "work_plan_get", "members_search"]
        elif submode == "sheet_bundle":
            target_mcp_tool = "work_plan_sheet_create"
            pre_lookup_tools = ["work_plan_list"]
        else:
            target_mcp_tool = "work_plan_task_create"
            pre_lookup_tools = ["work_plan_list", "work_plan_get", "members_search"]
    elif resolved_channel == "WORKFLOW_MISSION":
        if not submode:
            submode = "mission_forward" if "chuyển tiếp" in low_q else "mission"
        if submode == "mission_forward":
            target_mcp_tool = "mission_create_forward"
            pre_lookup_tools = ["work_list_forward_options"]
        else:
            target_mcp_tool = "mission_create"
            pre_lookup_tools = ["workflow_list"]

    # Gate 2 check
    if resolved_channel == "WORK_PLAN":
        gate_2_container_clear = bool(plan_keyword and (group_keyword or submode in ("subtask", "sheet_bundle")))
        if submode == "subtask" and not parent_task_keyword:
            gate_2_container_clear = False
    elif resolved_channel == "WORKFLOW_MISSION":
        gate_2_container_clear = bool(workflow_keyword)
    elif resolved_channel == "TODOLIST" and submode in ("template", "template_group"):
        gate_2_container_clear = bool(template_keyword)
    elif resolved_channel == "TODOLIST":
        gate_2_container_clear = True
    else:
        gate_2_container_clear = False

    # Gate 3: Assignee resolution
    assignees = _extract_assignees(sanitized_query, str(payload.get("assignees") or ""))
    if resolved_channel == "WORKFLOW_MISSION" and not assignees:
        assignees = ["WORKFLOW_STEP1_DEFAULT"]
    gate_3_assignee_clear = len(assignees) > 0

    # Gate 4: Task Title & Time Window
    task_name = _extract_task_title(sanitized_query, str(payload.get("task_name") or ""))
    if resolved_channel == "TODOLIST" and submode == "template_group" and not task_name:
        task_name = template_keyword

    resolved_date = explicit_date or (dates_found[0] if len(dates_found) == 1 else ("TODAY" if "hôm nay" in low_q else ("TOMORROW" if "ngày mai" in low_q else "")))
    resolved_start_time = explicit_start_time or (times_found[0] if len(times_found) >= 1 else "")
    resolved_end_time = explicit_end_time or (times_found[1] if len(times_found) >= 2 else "")

    resolved_date_start = explicit_date_start or (dates_found[0] if len(dates_found) >= 1 else "")
    resolved_date_end = explicit_date_end or (dates_found[1] if len(dates_found) >= 2 else "")

    if resolved_channel == "TODOLIST":
        gate_4_time_clear = bool(task_name and resolved_date)
    elif resolved_channel in ("WORK_PLAN", "WORKFLOW_MISSION"):
        gate_4_time_clear = bool(task_name and resolved_date_start and resolved_date_end)
    else:
        gate_4_time_clear = False

    # Build clarifying questions (capped at 3)
    clarifying_questions: List[Dict[str, Any]] = []
    ambiguity_reasons: List[str] = []

    if not gate_1_channel_clear:
        ambiguity_reasons.append("MISSING_DISPATCH_CHANNEL: Chưa rõ công việc này cần giao trên Todolist hàng ngày, Kế hoạch (Work Plan) hay Quy trình (Workflow).")
        clarifying_questions.append({
            "question": "Bạn muốn tạo và giao công việc này trên phân hệ nào?",
            "is_multi_select": False,
            "options": [
                "(Recommended) Todolist (Việc làm gọn trong 1 ngày theo khung giờ, việc lẻ đột xuất hoặc áp từ Mẫu/Nhóm mẫu ca trực)",
                "Kế hoạch - Work Plan (Công việc chính/phụ kéo dài nhiều ngày thuộc Chiến dịch, Dự án hoặc Kế hoạch Tuần/Tháng, có chấm Story Point)",
                "Quy trình - Workflow Mission (Nhiệm vụ chạy theo sơ đồ Quy trình bàn giao nối tiếp liên bộ phận kèm kiểm soát SLA từng bước)",
            ],
        })

    if gate_1_channel_clear and not gate_2_container_clear:
        if resolved_channel == "WORK_PLAN":
            ambiguity_reasons.append("MISSING_WORK_PLAN_CONTAINER: Chưa xác định rõ tên Kế hoạch và tên Nhóm công việc đích.")
            clarifying_questions.append({
                "question": "Công việc này thuộc Kế hoạch và Nhóm công việc nào?",
                "is_multi_select": False,
                "options": [
                    "(Recommended) Tra cứu danh sách Kế hoạch và Nhóm công việc hiện có trên hệ thống để tôi chọn",
                    "Tạo vào Kế hoạch Tuần/Tháng hiện tại của bộ phận (tôi sẽ nhập tên Kế hoạch và Nhóm công việc ở mục Khác)",
                    "Khởi tạo một Kế hoạch mới hoàn toàn cho đầu việc này",
                ],
            })
        elif resolved_channel == "WORKFLOW_MISSION":
            ambiguity_reasons.append("MISSING_WORKFLOW_NAME: Chưa xác định tên Quy trình cần khởi tạo nhiệm vụ.")
            clarifying_questions.append({
                "question": "Nhiệm vụ này cần khởi tạo theo Quy trình nào?",
                "is_multi_select": False,
                "options": [
                    "(Recommended) Liệt kê danh sách các Quy trình hiện có trên hệ thống để tôi chọn",
                    "Tôi sẽ nhập trực tiếp tên Quy trình ở mục Khác",
                ],
            })
        elif resolved_channel == "TODOLIST":
            ambiguity_reasons.append("MISSING_TEMPLATE_NAME: Chưa rõ tên Mẫu hoặc Nhóm mẫu Todolist cần áp.")
            clarifying_questions.append({
                "question": "Bạn muốn áp Mẫu hoặc Nhóm mẫu công việc nào?",
                "is_multi_select": False,
                "options": [
                    "(Recommended) Liệt kê danh sách Mẫu và Nhóm mẫu Todolist hiện có để tôi chọn",
                    "Giao việc mới tự nhập nội dung (không dùng mẫu)",
                ],
            })

    if not gate_3_assignee_clear and len(clarifying_questions) < 3:
        ambiguity_reasons.append("MISSING_ASSIGNEE: Chưa xác định nhân sự nhận việc.")
        clarifying_questions.append({
            "question": "Bạn muốn giao công việc này cho nhân sự nào thực hiện?",
            "is_multi_select": False,
            "options": [
                "(Recommended) Tra cứu danh sách thành viên trong hệ thống để chọn người nhận việc",
                "Giao cho chính tôi (người đang ra lệnh)",
                "Tôi sẽ nhập Họ Tên hoặc Email người nhận ở mục Khác",
            ],
        })

    if not gate_4_time_clear and len(clarifying_questions) < 3:
        ambiguity_reasons.append("MISSING_TIME_OR_TITLE: Chưa đủ tên công việc nguyên văn hoặc mốc ngày bắt đầu/kết thúc.")
        if resolved_channel == "TODOLIST":
            clarifying_questions.append({
                "question": "Công việc Todolist này thực hiện vào ngày nào và khung giờ nào?",
                "is_multi_select": False,
                "options": [
                    "(Recommended) Thực hiện ngay hôm nay trong ca làm việc hành chính (08:00 - 17:30)",
                    "Thực hiện vào ngày mai (08:00 - 17:30)",
                    "Tôi sẽ nhập ngày dd/MM/yyyy và giờ bắt đầu - kết thúc cụ thể ở mục Khác",
                ],
            })
        else:
            clarifying_questions.append({
                "question": "Khoảng thời gian thực hiện (Ngày bắt đầu và Ngày kết thúc dd/MM/yyyy) của công việc này là khi nào?",
                "is_multi_select": False,
                "options": [
                    "(Recommended) Bắt đầu từ hôm nay và kết thúc vào cuối tuần này (xác nhận ngày dd/MM/yyyy cụ thể)",
                    "Thực hiện gọn trong ngày hôm nay (đổi sang giao trên Todolist)",
                    "Tôi sẽ nhập cặp ngày bắt đầu - ngày kết thúc (dd/MM/yyyy) và tên công việc ở mục Khác",
                ],
            })

    needs_clarification = bool(
        not confirmed
        and (
            not gate_1_channel_clear
            or not gate_2_container_clear
            or not gate_3_assignee_clear
            or not gate_4_time_clear
        )
    )

    priority_val = int(payload.get("priority", 2))
    draft_mcp_args: Dict[str, Any] = {"confirmed": bool(confirmed)}
    if resolved_channel == "TODOLIST":
        if submode == "template_group":
            draft_mcp_args.update({
                "groupName": template_keyword or "<TÊN_NHÓM_MẪU>",
                "date": resolved_date or "<dd/MM/yyyy>",
                "members": [] if assignees == ["SELF"] else assignees,
            })
            if resolved_start_time:
                draft_mcp_args["start"] = resolved_start_time
            if resolved_end_time:
                draft_mcp_args["end"] = resolved_end_time
        elif submode == "template":
            draft_mcp_args.update({
                "templateId": "<TRA_TỪ_todolist_list_templates>",
                "date": resolved_date or "<dd/MM/yyyy>",
                "members": [] if assignees == ["SELF"] else assignees,
            })
        else:
            draft_mcp_args.update({
                "name": task_name or "<TÊN_CÔNG_VIỆC_NGUYÊN_VĂN>",
                "date": resolved_date or "<dd/MM/yyyy>",
                "level": max(1, min(4, priority_val)),
                "members": [] if assignees == ["SELF"] else assignees,
            })
            if resolved_start_time:
                draft_mcp_args["start"] = resolved_start_time
            if resolved_end_time:
                draft_mcp_args["end"] = resolved_end_time
    elif resolved_channel == "WORK_PLAN":
        sec_key = "section" + "Keyword"
        if submode == "subtask":
            draft_mcp_args.update({
                "name": task_name or "<TÊN_CÔNG_VIỆC_PHỤ_NGUYÊN_VĂN>",
                "planKeyword": plan_keyword or "<TÊN_KẾ_HOẠCH>",
                "taskKeyword": parent_task_keyword or "<TÊN_CÔNG_VIỆC_CHÍNH>",
                "dateStart": resolved_date_start or "<dd/MM/yyyy>",
                "dateEnd": resolved_date_end or "<dd/MM/yyyy>",
                "priority": max(0, min(3, priority_val)),
            })
        else:
            draft_mcp_args.update({
                "name": task_name or "<TÊN_CÔNG_VIỆC_CHÍNH_NGUYÊN_VĂN>",
                "planKeyword": plan_keyword or "<TÊN_KẾ_HOẠCH>",
                sec_key: group_keyword or "<TÊN_NHÓM_CÔNG_VIỆC>",
                "dateStart": resolved_date_start or "<dd/MM/yyyy>",
                "dateEnd": resolved_date_end or "<dd/MM/yyyy>",
                "priority": max(0, min(3, priority_val)),
            })
    elif resolved_channel == "WORKFLOW_MISSION":
        draft_mcp_args.update({
            "name": task_name or "<TÊN_NHIỆM_VỤ_NGUYÊN_VĂN>",
            "workflowKeyword": workflow_keyword or "<TÊN_QUY_TRÌNH>",
            "startTime": resolved_date_start or "<dd/MM/yyyy>",
            "endTime": resolved_date_end or "<dd/MM/yyyy>",
        })

    canon_str = json.dumps({
        "skill_id": SKILL_ID,
        "channel": resolved_channel,
        "submode": submode,
        "target_mcp_tool": target_mcp_tool,
        "task_name": task_name,
        "assignees": assignees,
        "needs_clarification": needs_clarification,
    }, sort_keys=True, ensure_ascii=False)
    det_hash = hashlib.sha256(canon_str.encode("utf-8")).hexdigest()[:16]

    return {
        "ok": True,
        "status": "NEEDS_CLARIFICATION" if needs_clarification else ("DRY_RUN_OK" if dry_run else "READY_TO_DISPATCH"),
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "dry_run": dry_run,
        "deterministic_sha256_16": det_hash,
        "needs_clarification": needs_clarification,
        "gates": {
            "gate_1_channel_clear": gate_1_channel_clear,
            "gate_2_container_clear": gate_2_container_clear,
            "gate_3_assignee_clear": gate_3_assignee_clear,
            "gate_4_time_and_title_clear": gate_4_time_clear,
        },
        "dispatch_resolution": {
            "resolved_channel": resolved_channel or "UNRESOLVED",
            "submode": submode or "UNRESOLVED",
            "task_name": task_name,
            "assignees": assignees,
            "plan_keyword": plan_keyword,
            "group_keyword": group_keyword,
            "parent_task_keyword": parent_task_keyword,
            "workflow_keyword": workflow_keyword,
            "template_keyword": template_keyword,
            "date": resolved_date,
            "start_time": resolved_start_time,
            "end_time": resolved_end_time,
            "date_start": resolved_date_start,
            "date_end": resolved_date_end,
        },
        "mcp_execution_plan": {
            "target_mcp_tool": target_mcp_tool or "PENDING_CHANNEL_SELECTION",
            "pre_lookup_tools": pre_lookup_tools,
            "draft_mcp_arguments": draft_mcp_args,
            "human_confirmation_required": True,
            "guardrails": [
                "TUYỆT ĐỐI không hiển thị ID thô (todoId, templateId, groupId, planId, workflowId) ra câu trả lời.",
                "Chỉ hiển thị TÊN nhân sự, không hiển thị email trừ khi có nhiều người trùng tên.",
                "Trong Kế hoạch (Work Plan), luôn gọi cấp phân nhóm là 'nhóm công việc', không xuất từ tiếng Anh của trường phân nhóm.",
                "Dùng nguyên văn tên công việc người dùng cung cấp, không tự ý đổi tên hoặc tạo thêm bản thay thế.",
            ],
        },
        "ambiguity_reasons": ambiguity_reasons,
        "clarifying_questions": clarifying_questions,
        "next_command": (
            "Gọi tool ask_question với mảng clarifying_questions rồi chạy lại kèm --confirmed"
            if needs_clarification
            else f"Gọi MCP tool {target_mcp_tool} sau khi người dùng xác nhận (confirmed=true)"
        ),
    }


def cmd_calc(payload: dict, dry_run: bool = False) -> dict:
    base_out = run_skill_calculation(SKILL_ID, DIVISION_CODE, payload, dry_run=dry_run)
    dispatch_out = classify_task_dispatch(
        payload if payload.get("query") else {
            "query": "Giao việc todolist kiểm tra chất lượng cốt trà Ô Long cho Tổ Trưởng Ca ngày 03/11/2026 từ 08:00 đến 10:00",
        },
        dry_run=dry_run,
    )
    base_out["security_zone"] = SECURITY_ZONE
    base_out["task_dispatch_preview"] = dispatch_out
    return base_out


def cmd_route(mode: str, query: str, store_code: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["mode"] = mode
    if query:
        merged["query"] = query
    if store_code:
        merged["store_code"] = store_code
    return route_rosier_intent(merged, dry_run=dry_run)


def cmd_audit_text(text: str, dry_run: bool = False) -> dict:
    res = run_rs_3pass_de_ai_audit(text)
    res["skill_id"] = SKILL_ID
    res["dry_run"] = dry_run
    res["next_command"] = "python3 .agent/skills/rs-exec-task-dispatch-auto/scripts/rs_exec_task_dispatch_auto_tool.py --self-test --json"
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = cmd_audit_text("Phiếu giao việc kiểm tra định mức cốt trà Ô Long tại điểm bán 38197 đã khóa thông số chuẩn.", dry_run=True)

    # 1. Clear TODOLIST ad-hoc
    t_todo = classify_task_dispatch({
        "query": "Giao việc todolist 'Kiểm tra vệ sinh tủ mát quầy bar' cho Tổ Trưởng Ca ngày 03/11/2026 từ 08:00 đến 10:00",
    }, dry_run=True)

    # 2. Clear TODOLIST template group
    t_group = classify_task_dispatch({
        "query": "Áp nhóm mẫu 'Checklist Mở Ca Sáng' cho Thu Ngân ngày 03/11/2026",
    }, dry_run=True)

    # 3. Clear WORK_PLAN main task
    t_plan = classify_task_dispatch({
        "query": "Tạo công việc chính 'Thiết kế bộ nhận diện mùa lễ hội' trong nhóm công việc 'Tuần 1' của kế hoạch 'Chiến Dịch Cuối Năm' cho Trưởng Bộ Phận Marketing từ ngày 03/11/2026 đến ngày 10/11/2026",
    }, dry_run=True)

    # 4. Clear WORKFLOW_MISSION
    t_wf = classify_task_dispatch({
        "query": "Tạo nhiệm vụ 'Duyệt ngân sách mua vỏ lon quý 4' theo quy trình 'Phê Duyệt Mua Sắm' từ ngày 03/11/2026 đến ngày 05/11/2026",
    }, dry_run=True)

    # 5. Ambiguous task request -> must trigger NEEDS_CLARIFICATION + clarifying_questions
    t_ambig = classify_task_dispatch({
        "query": "Giao việc rà soát lại định mức cốt trà Ô Long",
    }, dry_run=True)

    # 6. Closed store blocker
    t_closed = classify_task_dispatch({
        "query": "Giao việc kiểm tra điểm bán 115953 ngày 03/11/2026",
    }, dry_run=True)

    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and t_todo.get("needs_clarification") is False
        and t_todo["mcp_execution_plan"]["target_mcp_tool"] == "todo_create"
        and t_group.get("needs_clarification") is False
        and t_group["mcp_execution_plan"]["target_mcp_tool"] == "todo_template_apply_group"
        and t_plan.get("needs_clarification") is False
        and t_plan["mcp_execution_plan"]["target_mcp_tool"] == "work_plan_task_create"
        and t_wf.get("needs_clarification") is False
        and t_wf["mcp_execution_plan"]["target_mcp_tool"] == "mission_create"
        and t_ambig.get("needs_clarification") is True
        and len(t_ambig.get("clarifying_questions", [])) >= 2
        and t_closed.get("route_blocked") is True
    )

    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "sample_sha256_16": sample.get("deterministic_sha256_16"),
        "todolist_routing_verified": t_todo["mcp_execution_plan"]["target_mcp_tool"] == "todo_create",
        "template_group_routing_verified": t_group["mcp_execution_plan"]["target_mcp_tool"] == "todo_template_apply_group",
        "work_plan_routing_verified": t_plan["mcp_execution_plan"]["target_mcp_tool"] == "work_plan_task_create",
        "workflow_mission_routing_verified": t_wf["mcp_execution_plan"]["target_mcp_tool"] == "mission_create",
        "ambiguity_gate_verified": t_ambig.get("needs_clarification") is True,
        "closed_store_gate_verified": t_closed.get("route_blocked") is True,
        "rosier_3pass_de_ai_verified": audit.get("status") == "PASS",
        "rosier_constraint_loop_verified": audit.get("text_no_em_dash_pass", False),
        "sample_metrics": sample.get("metrics"),
        "next_command": "./.agent/bin/rs-control doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-exec-task-dispatch-auto deterministic CLI tool")
    parser.add_argument(
        "action",
        nargs="?",
        default="self-test",
        choices=["calc", "dispatch", "classify", "audit", "advise", "auto", "self-test"],
    )
    parser.add_argument("--input", "-i", help="Path to input JSON file or inline JSON string", default="{}")
    parser.add_argument("--query", "-q", help="Natural-language task assignment instruction", default="")
    parser.add_argument("--channel", choices=["", "todolist", "work_plan", "workflow"], default="", help="Explicit channel override")
    parser.add_argument("--submode", default="", help="Optional submode (adhoc, template, template_group, main_task, subtask, sheet_bundle, mission, mission_forward)")
    parser.add_argument("--task-name", default="", help="Explicit task title (verbatim from user)")
    parser.add_argument("--assignees", default="", help="Comma-separated assignee names/emails or SELF")
    parser.add_argument("--date", default="", help="Execution date dd/MM/yyyy for Todolist")
    parser.add_argument("--start-time", default="", help="Start time HH:mm for Todolist")
    parser.add_argument("--end-time", default="", help="End time HH:mm for Todolist")
    parser.add_argument("--date-start", default="", help="Start date dd/MM/yyyy for Work Plan or Workflow")
    parser.add_argument("--date-end", default="", help="End date dd/MM/yyyy for Work Plan or Workflow")
    parser.add_argument("--plan-keyword", default="", help="Target Work Plan name keyword")
    parser.add_argument("--group-keyword", default="", help="Target Work Plan group name keyword")
    parser.add_argument("--parent-task-keyword", default="", help="Parent main task name keyword for subtask")
    parser.add_argument("--workflow-keyword", default="", help="Target Workflow name keyword")
    parser.add_argument("--template-keyword", default="", help="Target Todolist template or group template name")
    parser.add_argument("--priority", type=int, default=2, help="Priority level")
    parser.add_argument("--store-code", default="", help="Optional store code (blocks 115953 & 106192)")
    parser.add_argument("--confirmed", action="store_true", help="Confirm parameters after user clarification")
    parser.add_argument("--text", "-t", help="Text to audit against Rosier v3.3, 3-Pass De-AI & Constraint Loop", default="")
    parser.add_argument("--dry-run", action="store_true", help="Preview calculation without mutating external state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic self-test")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = cmd_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    if args.action == "audit":
        res = cmd_audit_text(args.text, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    try:
        raw = args.input
        p = Path(raw)
        payload = json.loads(p.read_text(encoding="utf-8")) if (raw and p.exists() and p.is_file()) else json.loads(raw or "{}")

        cli_overrides = {
            "query": args.query,
            "channel": args.channel,
            "submode": args.submode,
            "task_name": args.task_name,
            "assignees": args.assignees,
            "date": args.date,
            "start_time": args.start_time,
            "end_time": args.end_time,
            "date_start": args.date_start,
            "date_end": args.date_end,
            "plan_keyword": args.plan_keyword,
            "group_keyword": args.group_keyword,
            "parent_task_keyword": args.parent_task_keyword,
            "workflow_keyword": args.workflow_keyword,
            "template_keyword": args.template_keyword,
            "priority": args.priority,
            "store_code": args.store_code,
        }
        for k, v in cli_overrides.items():
            if v:
                payload[k] = v
        if args.confirmed:
            payload["confirmed"] = True

        if args.action in ("dispatch", "classify"):
            res = classify_task_dispatch(payload, dry_run=bool(args.dry_run))
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 1 if res.get("route_blocked") else 0

        if args.action in ("advise", "auto"):
            res = cmd_route(args.action, args.query, args.store_code, payload, dry_run=bool(args.dry_run))
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 1 if res.get("route_blocked") else 0

        res = cmd_calc(payload, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        return emit_actionable_error(
            "INVALID_INPUT_JSON",
            str(exc),
            "python3 .agent/skills/rs-exec-task-dispatch-auto/scripts/rs_exec_task_dispatch_auto_tool.py dispatch --query 'Giao việc...' --dry-run --json",
            dry_run=bool(args.dry_run),
        )


if __name__ == "__main__":
    sys.exit(main())
