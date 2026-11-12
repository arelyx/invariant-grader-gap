"""Run UAutomizer on candidates that do not have full-verifier verdicts yet.

usage: python src/run_full.py <candidates.jsonl> <out.jsonl> [workers=14] [queries=correct|both]
Identical (instance, invariant) pairs are checked once. Timeouts: 30 s easy, 120 s hard,
the same limits as the 2026-11-10 runs. Appends; safe to re-run.
"""
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import paths
import queries
from full_grader import run_uautomizer

cand_path, out_path = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 14
both = len(sys.argv) > 4 and sys.argv[4] == "both"
TIMEOUT = {"easy": 30, "hard": 120}

inst = {i["id"]: i for i in json.load(open(paths.DATA / "instances.json"))}
cands = [json.loads(l) for l in open(cand_path)]
done = set()
try:
    done = {(r["instance"], r["invariant"]) for r in map(json.loads, open(out_path))}
except FileNotFoundError:
    pass
uniq = {}
for c in cands:
    if c["valid"]:
        uniq.setdefault((c["instance"], c["invariant"]), c)
jobs = [k for k in uniq if k not in done]
# easy programs first so partial results cover a whole split
jobs.sort(key=lambda k: inst[k[0]]["split"] != "easy")
print("unique valid pairs", len(uniq), "to run", len(jobs), flush=True)
lock = threading.Lock()
out = open(out_path, "a")


def one(key):
    iid, inv = key
    i = inst[iid]
    prog = queries.build_program(i["original_program"])
    to = TIMEOUT[i["split"]]
    rc = run_uautomizer(queries.correctness_query(prog, i["marker"], inv), to)
    row = {"instance": iid, "invariant": inv, "split": i["split"],
           "full_correct": rc["decision"], "t_correct": rc["seconds"]}
    if both:
        rs = run_uautomizer(queries.sufficiency_query(prog, i["marker"], inv), to)
        row.update(full_sufficient=rs["decision"], t_sufficient=rs["seconds"])
    with lock:
        out.write(json.dumps(row) + "\n")
        out.flush()


with ThreadPoolExecutor(workers) as ex:
    list(ex.map(one, jobs))
print("done")
