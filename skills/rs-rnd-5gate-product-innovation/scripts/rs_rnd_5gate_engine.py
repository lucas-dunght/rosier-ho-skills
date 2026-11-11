#!/usr/bin/env python3
"""
Bundled Deterministic Engine Module for rs-rnd-5gate-product-innovation (rs_rnd_5gate_engine.py).
Delegates to core.rs_core_engine.execute_rnd_5gate_action and execute_bom_lifecycle_action.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    RND_5GATE_ACTIONS,
    convert_numbers_to_vietnamese_spoken,
    execute_bom_lifecycle_action,
    execute_rnd_5gate_action,
    load_rnd_innovation_ledger,
)


def run_engine(payload: Dict[str, Any], dry_run: bool = False, is_ho_edition: bool = False) -> Dict[str, Any]:
    return execute_rnd_5gate_action(payload, dry_run=dry_run, is_ho_edition=is_ho_edition)
