#!/bin/bash
cd "$(dirname "$0")/../src"
exec ../.venv/bin/python run_cheap.py ../data/candidates_w4b8.jsonl ../results/cheap_w4b8.jsonl 1,2,5,10,20,50 12 30
