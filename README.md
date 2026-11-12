# Bounded check versus full verifier on model-written loop invariants

CSE 216 (Formal Methods, UCSC, Fall 2026), Team 10 course project. Preliminary work.

## Question

Small language models are trained to write loop invariants for C programs, and the training
signal is an automatic grader. A full verifier is slow, so a bounded model checker is used as a
cheaper grader. A bounded check can accept a false invariant when the violation needs more loop
iterations than the bound. We measure how often that happens on invariants that small models
write, and how it changes with the bound.

The question comes from the limitations section of the Loop-R1 preprint, which uses ESBMC with
bound k < 10 in its reward and says this "may introduce false positives". We found no
measurement of how many. No model training is involved here.

## Preliminary results

See `results/summary.md` (all tables), `results/examples.md` (concrete cases) and
`docs/project_summary.pdf` (write-up). Headline numbers are in the write-up, section 5.

3,935 valid candidates graded by both tools (UAutomizer: 1,628 proved, 2,016 wrong, 291 no answer).

| bound k | wrong invariants the bounded check accepts |
|---|---|
| 1 | 737 / 2,016 (36.6%) |
| 2 | 119 / 2,016 (5.9%) |
| 5 | 27 / 2,016 (1.3%) |
| 10 | 27 / 2,016 (1.3%, 95% interval 0.9 to 1.9) |
| 50 | 10 / 2,016 (0.5%) |

- Of the 27 at k=10, 4 are true bound effects (one loop, caught at k=50). The other 23 are
  pointer-versus-zero comparisons on list programs that a larger bound does not catch.
- 34 candidates were proved by UAutomizer and rejected by ESBMC; the ones inspected are signed
  overflow.
- Among proved invariants, ESBMC times out on 12.8% at k=10 and 41.7% at k=50.
- Picking one of 8 samples per loop: first sample is proved 46.4% of the time, first sample
  accepted at k=10 is proved 69.9%, best possible 76.5%.

## How it works

For each candidate invariant we build one C file, the *correctness query*: the original program
with `assert(candidate)` at the top of the loop body. Both graders check that same file.

| | Full grader | Cheap grader |
|---|---|---|
| Tool | UAutomizer (SV-COMP 2025 release) | ESBMC 8.6 |
| Explores | all executions | executions with at most k entries into each loop body |
| Answers | TRUE, FALSE, or no answer | ACCEPT, REJECT, or no answer |
| Time limit | 30 s easy loops, 120 s hard loops | 30 s |

A candidate is counted as wrong only when UAutomizer returns FALSE. Timeouts are a separate
category for both tools.

## Layout

```
src/paths.py          where the external tools live
src/queries.py        builds the correctness and sufficiency queries (uses Wonda's AstProgram)
src/cheap_grader.py   ESBMC bounded check, flags and verdict parsing
src/full_grader.py    UAutomizer wrapper
src/generate.py       samples candidate invariants from a model served by vLLM
src/run_cheap.py      bounded check over a candidates file, at several bounds
src/run_full.py       UAutomizer over a candidates file
src/analyze.py        joins both verdicts, counts disagreements, writes results/
scripts/setup.sh      fetches Wonda, UAutomizer and ESBMC into third_party/
scripts/gen_batch.sh  serve one model, sample, stop the server
scripts/import_prior_runs.py   imports the candidates graded on 2026-11-10
scripts/show_query.py prints the C file for one candidate
data/instances.json   362 loops from 219 InvBench programs (from the Wonda evaluation set)
data/candidates*.jsonl  sampled invariants; batch 1 already carries UAutomizer verdicts
results/              raw verdicts (jsonl), summary tables, examples, figure
docs/                 LaTeX write-up
```

## Reproduce

```bash
scripts/setup.sh                                  # tools into third_party/, Python env
cd src
python run_cheap.py ../data/candidates.jsonl ../results/cheap_single.jsonl
python run_full.py  ../data/candidates_w4b8.jsonl ../results/full_w4b8.jsonl
python run_cheap.py ../data/candidates_w4b8.jsonl ../results/cheap_w4b8.jsonl
python analyze.py
```

Sampling new candidates needs a GPU and vLLM: `scripts/gen_batch.sh <tag> <hf model> <n>`.

## Things that changed the numbers

1. ESBMC lets `malloc` fail by default and UAutomizer does not. Fixed with `--force-malloc-success`.
2. ESBMC wraps signed integers; UAutomizer proved invariants that are false under wraparound.
   With ESBMC's `--ir` (mathematical integers) the three cases we tested agree again. Not fixed;
   reported as its own category.
3. The benchmark programs use `NULL` without a header. ESBMC needs a one-line definition.

## Known limits

- The bounded check is our reconstruction of one sentence in the Loop-R1 preprint. Their code is
  not public and their reward has other terms we do not reproduce.
- 103 of the 362 loops are in programs whose loops are capped by a small constant, where a
  bounded check is complete once k reaches the cap.
- Both graders ran at the same time on one 32-core machine, so some timeouts may be load.
- All models are Qwen3 based.

## Credits and data

Programs and prompt come from [Wonda](https://github.com/idopinto/wonda) (MIT) and InvBench
(Quokka, arXiv:2509.21629). Verifiers: [Ultimate Automizer](https://ultimate-pa.org) and
[ESBMC](https://github.com/esbmc/esbmc).

## Note on authorship

The code and notes in this repository were drafted with an AI assistant. The course report must
be written by the team in their own words, and the team must be able to explain every line here.
