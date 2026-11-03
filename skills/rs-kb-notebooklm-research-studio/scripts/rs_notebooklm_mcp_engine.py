#!/usr/bin/env python3
"""
Rosier NotebookLM MCP Orchestration Engine (rs_notebooklm_mcp_engine.py)
Coordinates 53 tools across 16 groups of notebooklm-mcp v0.15.8 with 9 Rosier F&B Archetypes (N1..N9),
HO Destructive-Tool Blocking, and Air-Gapped 2-Hub Sanitization.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    HO_FORBIDDEN_NOTEBOOKLM_TOOLS,
    NOTEBOOKLM_MCP_RUNTIME_META,
    NOTEBOOKLM_MCP_TOOLS_MAP,
    ROSIER_NOTEBOOKLM_ARCHETYPES_9,
    build_notebooklm_mcp_execution_plan,
)

__all__ = [
    "HO_FORBIDDEN_NOTEBOOKLM_TOOLS",
    "NOTEBOOKLM_MCP_RUNTIME_META",
    "NOTEBOOKLM_MCP_TOOLS_MAP",
    "ROSIER_NOTEBOOKLM_ARCHETYPES_9",
    "build_notebooklm_mcp_execution_plan",
    "get_notebooklm_engine_meta",
]


def get_notebooklm_engine_meta() -> Dict[str, Any]:
    return {
        "engine": "rs_notebooklm_mcp_engine",
        "runtime": NOTEBOOKLM_MCP_RUNTIME_META,
        "archetypes_count": len(ROSIER_NOTEBOOKLM_ARCHETYPES_9),
        "tool_groups_count": len(NOTEBOOKLM_MCP_TOOLS_MAP),
        "ho_forbidden_tools": list(HO_FORBIDDEN_NOTEBOOKLM_TOOLS),
    }
