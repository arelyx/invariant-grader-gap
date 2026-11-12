"""Print the correctness query for one candidate id (cid). usage: python scripts/show_query.py <cid> [candidates file]"""
import json, sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1] / "src"))
import paths, queries
cid = sys.argv[1]
f = sys.argv[2] if len(sys.argv) > 2 else paths.DATA / "candidates.jsonl"
c = next(c for c in map(json.loads, open(f)) if c["cid"] == cid)
i = {i["id"]: i for i in json.load(open(paths.DATA / "instances.json"))}[c["instance"]]
print(queries.correctness_query(queries.build_program(i["original_program"]), i["marker"], c["invariant"]))
