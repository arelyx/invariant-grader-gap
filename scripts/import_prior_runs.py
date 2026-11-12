"""One-off: import the candidates already graded by UAutomizer on 2026-11-10.

Source: ../experiments/wonda/runs/full (362 loop instances x 3 untrained Qwen3 models x 1 sample,
Wonda prompt and sampling settings, UAutomizer timeouts 30 s easy / 120 s hard).
Writes data/instances.json and data/candidates.jsonl.
"""
import json
import shutil
import sys
from pathlib import Path

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "experiments/wonda/runs/full"
DATA = Path(__file__).resolve().parents[1] / "data"
MODELS = {"q06b": "Qwen/Qwen3-0.6B", "q17b": "Qwen/Qwen3-1.7B", "q4bi": "Qwen/Qwen3-4B-Instruct-2507"}
shutil.copy(SRC / "instances.json", DATA / "instances.json")
shutil.copy(SRC / "baseline.json", DATA / "baseline_no_invariant.json")
n = 0
with open(DATA / "candidates.jsonl", "w") as out:
    for tag, model in MODELS.items():
        for r in json.load(open(SRC / f"analyzed2_{tag}.json")):
            row = {"cid": f"{tag}:{r['id']}:{r['sample']}", "batch": "single", "model": model,
                   "instance": r["id"], "sample": r["sample"], "split": r["split"], "raw": r["raw"],
                   "valid": r["valid"], "invariant": r["invariant"], "target": r["target"],
                   "full_correct": r.get("corr_decision"), "full_sufficient": r.get("suff_decision"),
                   "t_correct": r.get("t_corr"), "t_sufficient": r.get("t_suff"),
                   "restates_target": r.get("restate_cat")}
            out.write(json.dumps(row) + "\n")
            n += 1
print("wrote", n, "candidates")
