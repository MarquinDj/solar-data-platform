from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA = PROJECT_ROOT / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"

RAW_TEST = RAW / "test"
PROCESSED_TEST = PROCESSED / "test"
