"""Where the external tools live. Override with environment variables if needed."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THIRD = Path(os.environ.get("IGG_THIRD_PARTY", ROOT / "third_party"))
WONDA = THIRD / "wonda"                                   # github.com/idopinto/wonda (MIT)
ULTIMATE = THIRD / "uautomizer" / "UAutomizer-linux" / "Ultimate.py"   # SV-COMP 2025 release
ESBMC = THIRD / "esbmc" / "release" / "bin" / "esbmc"     # ESBMC v8.6
PRP = WONDA / "data" / "properties" / "unreach-call.prp"
DATA = ROOT / "data"
RESULTS = ROOT / "results"
TMP = ROOT / "runs" / "tmp"

sys.path.insert(0, str(WONDA))
