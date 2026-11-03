#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-kb-notebooklm-research-studio: Xưởng Nghiên Cứu Tri Thức, Sản Xuất Học Liệu Studio & Bóc Băng Ghi Âm Trên Google NotebookLM MCP
Part of Rosier Master Skill Ecosystem (RS-OS 200 · Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    build_audio_diarization_mcp_plan,
    build_notebooklm_mcp_execution_plan,
    diarize_and_attribute_rosier_transcript,
    execute_notebooklm_action,
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-kb-notebooklm-research-studio"
DIVISION_CODE = "02"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"

NLM_STUDIO_ACTIONS = (
    "plan",
    "archetypes",
    "slots",
    "compile-prompts",
    "diarize",
    "audio-plan",
)


def is_ho_repository() -> bool:
    """Detect whether the current execution environment is the Head Office (Khối HO) repository."""
    return (SUITE_ROOT / "rules" / "rs-ho-auto-router.md").exists()


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_kb_notebooklm_research_studio_tool.py]",
        "skill_id": SKILL_ID,
        "dry_run": dry_run,
        "error": {
            "code": code,
            "root_cause": root_cause,
            "next_command": next_command,
        },
    }, ensure_ascii=False, indent=2))
    return 1


def cmd_calc(payload: dict, dry_run: bool = False) -> dict:
    out = run_skill_calculation(SKILL_ID, DIVISION_CODE, payload, dry_run=dry_run)
    out["security_zone"] = SECURITY_ZONE
    return out


def cmd_nlm(action: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["nlm_action"] = action
    is_ho = is_ho_repository() or bool(merged.get("is_ho_edition", False))
    res = execute_notebooklm_action(merged, dry_run=dry_run, is_ho_edition=is_ho)
    res["skill_id"] = SKILL_ID
    res["division_code"] = DIVISION_CODE
    res["security_zone"] = SECURITY_ZONE
    res["is_ho_edition"] = is_ho
    return res


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
    res["next_command"] = "python3 scripts/rs_kb_notebooklm_research_studio_tool.py --self-test --json"
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = cmd_audit_text(
        "Sổ tay NotebookLM trích xuất quy trình pha chế Trà Ô Long Nhài Sữa và câu hỏi trắc nghiệm Bloom cho 25 điểm bán.",
        dry_run=True,
    )
    arch_res = execute_notebooklm_action({"nlm_action": "archetypes"}, dry_run=True)
    plan_res = build_notebooklm_mcp_execution_plan(
        {"archetype_id": "N3", "topic": "Học liệu SOP Trà Ô Long Nhài Sữa và giá vốn COGS", "target_hub": "ROSIER_STORE_HUB"},
        is_ho_edition=True,
    )
    ho_block = build_notebooklm_mcp_execution_plan({"mcp_tool": "notebook_delete"}, is_ho_edition=True)
    diar_res = diarize_and_attribute_rosier_transcript({})
    audio_plan = build_audio_diarization_mcp_plan({}, is_ho_edition=False)

    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and arch_res.get("total_archetypes") == 9
        and arch_res.get("total_speaker_fingerprints") == 9
        and plan_res.get("ok") is True
        and plan_res.get("mcp_sequence_steps_count") == 8
        and plan_res.get("store_hub_air_gap_sanitized") is True
        and ho_block.get("status") == "BLOCKED"
        and ho_block.get("error", {}).get("code") == "HO_DESTRUCTIVE_NOTEBOOKLM_TOOL_FORBIDDEN"
        and diar_res.get("ok") is True
        and diar_res.get("role_only_zero_personal_names") is True
        and audio_plan.get("ok") is True
    )
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "is_ho_edition": is_ho_repository(),
        "sample_sha256_16": sample.get("deterministic_sha256_16"),
        "rosier_3pass_de_ai_verified": audit.get("status") == "PASS",
        "rosier_constraint_loop_verified": audit.get("text_no_em_dash_pass", False),
        "notebooklm_9_archetypes_verified": arch_res.get("total_archetypes") == 9,
        "notebooklm_8step_mcp_plan_verified": plan_res.get("mcp_sequence_steps_count") == 8,
        "notebooklm_ho_destructive_guard_verified": ho_block.get("status") == "BLOCKED",
        "notebooklm_audio_diarization_9roles_verified": diar_res.get("role_only_zero_personal_names") is True,
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="rs-kb-notebooklm-research-studio deterministic CLI tool (Google NotebookLM MCP v0.15.8 Orchestrator & 4-Step Audio Diarization Engine)"
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="self-test",
        choices=["calc", "audit", "advise", "auto", "self-test", *NLM_STUDIO_ACTIONS],
    )
    parser.add_argument("--input", "-i", help="Path to input JSON file or inline JSON string", default="{}")
    parser.add_argument("--query", "-q", help="Natural-language task or content for advise/auto routing", default="")
    parser.add_argument("--store-code", help="Store code for context verification (e.g., 38197, 67650)", default="")
    parser.add_argument("--archetype", "--archetype-id", dest="archetype_id", help="Rosier NotebookLM Archetype ID (N1..N9)", default="N1")
    parser.add_argument("--topic", help="Research or Studio generation topic", default="")
    parser.add_argument("--target-hub", help="Target Knowledge Hub (ROSIER_BUSINESS or ROSIER_STORE_HUB)", default="")
    parser.add_argument("--persona-id", help="Rosier Persona ID (e.g., rs-persona-first-principles-truth, rs-persona-master-rnd)", default="")
    parser.add_argument("--mcp-tool", help="Specific NotebookLM MCP tool name to validate/plan", default="")
    parser.add_argument("--notebook-id", help="Target NotebookLM UUID", default="")
    parser.add_argument("--audio-source", help="Path or URL to meeting audio recording for N9 diarization", default="")
    parser.add_argument("--transcript", help="Raw transcript text for 4-step STT normalization and speaker diarization", default="")
    parser.add_argument("--text", "-t", help="Vietnamese text to audit with Rosier 3-Pass De-AI Scanner", default="")
    parser.add_argument("--dry-run", action="store_true", help="Preview deterministic output without mutating state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic self-test")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        report = cmd_self_test()
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "PASS" else 1

    raw = args.input.strip()
    try:
        if raw.startswith("{"):
            payload = json.loads(raw)
        else:
            p = Path(raw)
            payload = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    except Exception as exc:
        return emit_actionable_error(
            "INVALID_JSON_INPUT",
            f"Could not parse --input JSON: {exc}",
            "python3 scripts/rs_kb_notebooklm_research_studio_tool.py --self-test --json",
            dry_run=args.dry_run,
        )

    if args.store_code:
        payload["store_code"] = args.store_code
    if args.archetype_id:
        payload["archetype_id"] = args.archetype_id
    if args.topic:
        payload["topic"] = args.topic
    if args.target_hub:
        payload["target_hub"] = args.target_hub
    if args.persona_id:
        payload["persona_id"] = args.persona_id
    if args.mcp_tool:
        payload["mcp_tool"] = args.mcp_tool
    if args.notebook_id:
        payload["notebook_id"] = args.notebook_id
    if args.audio_source:
        payload["audio_source"] = args.audio_source
    if args.transcript:
        payload["transcript"] = args.transcript

    if args.action in NLM_STUDIO_ACTIONS:
        out = cmd_nlm(args.action, payload, dry_run=args.dry_run)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if out.get("ok", True) else 1

    if args.action == "audit":
        target_text = args.text or payload.get("text", "Trà Ô Long Nhài Sữa ủ lạnh ở 4 độ C.")
        out = cmd_audit_text(target_text, dry_run=args.dry_run)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    if args.action in ("advise", "auto"):
        out = cmd_route(args.action, args.query, args.store_code, payload, dry_run=args.dry_run)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if not out.get("route_blocked", False) else 1

    out = cmd_calc(payload, dry_run=args.dry_run)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
