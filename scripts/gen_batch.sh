#!/bin/bash
# Serve one model with vLLM, sample N invariants per loop, stop the server (by PID).
# usage: scripts/gen_batch.sh <tag> <hf model> <n> [gpu fraction]
cd "$(dirname "$0")/.."
VLLM=${VLLM:-/home/arelyx/cse216-project/experiments/pilot/.venv/bin/vllm}
setsid $VLLM serve "$2" --port 8123 --max-model-len 8192 --gpu-memory-utilization ${4:-0.85} \
  --served-model-name pilot > results/vllm_$1.log 2>&1 < /dev/null &
SP=$!
for i in $(seq 1 240); do curl -s localhost:8123/v1/models > /dev/null && break; kill -0 $SP || exit 1; sleep 5; done
(cd src && ../.venv/bin/python generate.py "$1" "$2" "$3" ../data/candidates_$1.jsonl)
kill $SP; for i in $(seq 1 30); do kill -0 $SP 2>/dev/null || break; sleep 1; done
