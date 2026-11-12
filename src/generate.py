"""Sample candidate invariants from a model served by vLLM (OpenAI-compatible API on port 8123).

Prompt and sampling settings are Wonda's (configs/eval/prompts/wonda.yaml, hf_qwen_nt.yaml):
max 1024 new tokens, temperature 0.7, top_p 0.8, top_k 20, repetition penalty 1.1, thinking off.
usage: python src/generate.py <tag> <model name for the record> <n_samples> <out.jsonl>
"""
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import paths
from wonda.eval.validate import validate_model_answer


def yaml_block(path, key):
    out, on = [], False
    for ln in open(path).read().split("\n"):
        if ln.startswith(key + ":"):
            on = True
            continue
        if on:
            if ln and not ln.startswith(" "):
                break
            out.append(ln)
    ind = min(len(l) - len(l.lstrip()) for l in out if l.strip())
    return "\n".join(l[ind:] for l in out).rstrip("\n") + "\n"


tag, model, n, out_path = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
PROMPTS = paths.WONDA / "configs/eval/prompts/wonda.yaml"
SYS = yaml_block(PROMPTS, "per_marker_system_prompt")
USR = yaml_block(PROMPTS, "per_marker_user_prompt_template")
inst = json.load(open(paths.DATA / "instances.json"))


def call(i):
    body = {"model": "pilot", "n": n, "max_tokens": 1024, "temperature": 0.7, "top_p": 0.8, "top_k": 20,
            "min_p": 0, "repetition_penalty": 1.1, "chat_template_kwargs": {"enable_thinking": False},
            "messages": [{"role": "system", "content": SYS},
                         {"role": "user", "content": USR.format(program=i["llm_code"], target_marker=i["marker"])}]}
    req = urllib.request.Request("http://localhost:8123/v1/chat/completions", json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=900))
    rows = []
    for j, c in enumerate(r["choices"]):
        raw = c["message"]["content"]
        parsed, vd = validate_model_answer(raw, i["marker"])
        valid = bool(vd["valid_json_format"] and vd["valid_content"] and vd["valid_marker"])
        rows.append({"cid": f"{tag}:{i['id']}:{j}", "batch": tag, "model": model, "instance": i["id"], "sample": j,
                     "split": i["split"], "raw": raw, "valid": valid,
                     "invariant": parsed.content if parsed else None})
    return rows


with ThreadPoolExecutor(16) as ex, open(out_path, "w") as out:
    for rows in ex.map(call, inst):
        for r in rows:
            out.write(json.dumps(r) + "\n")
print("done")
