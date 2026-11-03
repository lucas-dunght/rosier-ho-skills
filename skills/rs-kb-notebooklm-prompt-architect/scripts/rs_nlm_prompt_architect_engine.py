#!/usr/bin/env python3
"""
Rosier NotebookLM v0.15.8 5-Block Grounded Prompt Architect Engine (rs_nlm_prompt_architect_engine.py)
Compiles 12 Prompt Slots with 3-Pass De-AI Guard and Air-Gapped 2-Hub Sanitization.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    NOTEBOOKLM_MCP_RUNTIME_META,
    ROSIER_NLM_PROMPT_SLOTS_V0158,
    ROSIER_NOTEBOOKLM_ARCHETYPES_9,
    compile_notebooklm_v0158_prompt_bundle,
)

__all__ = [
    "NOTEBOOKLM_MCP_RUNTIME_META",
    "ROSIER_NLM_PROMPT_SLOTS_V0158",
    "ROSIER_NOTEBOOKLM_ARCHETYPES_9",
    "compile_notebooklm_v0158_prompt_bundle",
    "get_prompt_architect_meta",
]


def get_prompt_architect_meta() -> Dict[str, Any]:
    return {
        "engine": "rs_nlm_prompt_architect_engine",
        "runtime": NOTEBOOKLM_MCP_RUNTIME_META,
        "total_prompt_slots": len(ROSIER_NLM_PROMPT_SLOTS_V0158),
        "prompt_slots": list(ROSIER_NLM_PROMPT_SLOTS_V0158.keys()),
    }
