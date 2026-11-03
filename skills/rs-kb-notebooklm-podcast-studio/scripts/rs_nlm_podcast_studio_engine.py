#!/usr/bin/env python3
"""
Bundled Deterministic Engine Module for rs-kb-notebooklm-podcast-studio (rs_nlm_podcast_studio_engine.py).
Delegates to core.rs_core_engine.build_notebooklm_podcast_studio_plan and execute_notebooklm_creative_lms_action.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    build_notebooklm_podcast_studio_plan,
    convert_numbers_to_vietnamese_spoken,
    execute_notebooklm_creative_lms_action,
)


def run_engine(payload: Dict[str, Any], is_ho_edition: bool = False) -> Dict[str, Any]:
    return build_notebooklm_podcast_studio_plan(payload, is_ho_edition=is_ho_edition)
