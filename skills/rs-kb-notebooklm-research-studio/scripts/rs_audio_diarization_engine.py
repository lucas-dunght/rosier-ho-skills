#!/usr/bin/env python3
"""
Rosier 4-Step Multi-Signal Audio Speaker Diarization & STT Phonetic Normalizer (rs_audio_diarization_engine.py)
100% Role-Only Speaker Attribution across 9 Rosier Roles (0% Personal Names, 0% Vendor Leaks).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    ROSIER_SPEAKER_FINGERPRINTS_9,
    ROSIER_STT_PHONETIC_CORRECTIONS,
    build_audio_diarization_mcp_plan,
    diarize_and_attribute_rosier_transcript,
    normalize_rosier_stt_transcript,
)

__all__ = [
    "ROSIER_SPEAKER_FINGERPRINTS_9",
    "ROSIER_STT_PHONETIC_CORRECTIONS",
    "build_audio_diarization_mcp_plan",
    "diarize_and_attribute_rosier_transcript",
    "normalize_rosier_stt_transcript",
    "get_diarization_engine_meta",
]


def get_diarization_engine_meta() -> Dict[str, Any]:
    return {
        "engine": "rs_audio_diarization_engine",
        "speaker_fingerprints_count": len(ROSIER_SPEAKER_FINGERPRINTS_9),
        "stt_phonetic_rules_count": len(ROSIER_STT_PHONETIC_CORRECTIONS),
        "role_only_zero_personal_names": True,
    }
