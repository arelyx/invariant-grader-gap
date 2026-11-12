"""Run the bounded check on every valid candidate, at several bounds.

usage: python src/run_cheap.py <candidates.jsonl> <out.jsonl> [bounds=1,2,5,10,20,50] [workers=16] [timeout=30]
Appends one line per (candidate, bound); safe to re-run, finished pairs are skipped.
"""
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import paths
import queries
from cheap_grader import bounded_check

cand_path, out_path = sys.argv[1], sys.argv[2]
bounds = [int(b) for b in (sys.argv[3] if len(sys.argv) > 3 else "1,2,5,10,20,50").split(",")]
workers = int(sys.argv[4]) if len(sys.argv) > 4 else 16
timeout = float(sys.argv[5]) if len(sys.argv) > 5 else 30.0

inst = {i["id"]: i for i in json.load(open(paths.DATA / "instances.json"))}
cands = [json.loads(l) for l in open(cand_path)]
done = set()
try:
    for l in open(out_path):
        r = json.loads(l)
        done.add((r["cid"], r["k"]))
except FileNotFoundError:
    pass
lock = threading.Lock()
out = open(out_path, "a")


# identical (loop, invariant) pairs are checked once and the verdict is written for every sample
groups = {}
for c in cands:
    if c["valid"]:
        groups.setdefault((c["instance"], c["invariant"]), []).append(c)


def one(key):
    group = groups[key]
    todo = [k for k in bounds if any((c["cid"], k) not in done for c in group)]
    if not todo:
        return
    i = inst[key[0]]
    q = queries.correctness_query(queries.build_program(i["original_program"]), i["marker"], key[1])
    carried = None
    for k in sorted(todo):
        # a violation found within k iterations is also within any larger bound, and a
        # timeout at k is treated as a timeout at larger k (marked "carried")
        r = {**carried, "seconds": 0.0, "carried": True} if carried else bounded_check(q, k, timeout)
        if r["verdict"] in ("REJECT", "TIMEOUT"):
            carried = r
        with lock:
            for c in group:
                if (c["cid"], k) not in done:
                    out.write(json.dumps({"cid": c["cid"], "k": k, **r}) + "\n")
            out.flush()


with ThreadPoolExecutor(workers) as ex:
    list(ex.map(one, list(groups)))
print("done")
