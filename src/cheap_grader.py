"""Cheap grader: bounded model checking with ESBMC.

Loop-R1 (preprint) describes one reward term as "bounded model checking via ESBMC with
bounded unwinding k < 10". Their code is not public, so this is our reading of that sentence:
run ESBMC on the correctness query with --unwind k and without unwinding assertions, so
executions longer than k loop iterations are simply not explored.

Verdicts:
  ACCEPT   ESBMC prints VERIFICATION SUCCESSFUL (no violation within the bound)
  REJECT   ESBMC prints VERIFICATION FAILED (found a violating execution)
  TIMEOUT  no answer within the time limit
  ERROR    parse error or anything else
"""
import os
import signal
import subprocess
import tempfile
import time

import paths

FLAGS = ["--32", "--no-unwinding-assertions",
         # only the assert() counts, as with UAutomizer's unreach-call property
         "--no-pointer-check", "--no-bounds-check", "--no-div-by-zero-check",
         # UAutomizer assumes malloc never returns NULL; ESBMC by default lets it fail.
         # Without this flag ESBMC rejects invariants like `x != NULL` that UAutomizer proves.
         "--force-malloc-success"]


# the benchmark programs use NULL without including a header; UAutomizer accepts that, ESBMC does not
PRELUDE = "#ifndef NULL\n#define NULL ((void *)0)\n#endif\n"


def bounded_check(c_code: str, k: int, timeout: float = 30.0) -> dict:
    os.makedirs(paths.TMP, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".c", dir=paths.TMP, delete=False) as f:
        f.write(PRELUDE + c_code)
        src = f.name
    cmd = [str(paths.ESBMC), src, "--unwind", str(k), *FLAGS]
    t0 = time.monotonic()
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                         start_new_session=True)
    try:
        out, _ = p.communicate(timeout=timeout)
        if "VERIFICATION SUCCESSFUL" in out:
            verdict = "ACCEPT"
        elif "VERIFICATION FAILED" in out:
            verdict = "REJECT"
        else:
            verdict = "ERROR"
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        p.wait()
        out, verdict = "", "TIMEOUT"
    os.unlink(src)
    return {"verdict": verdict, "seconds": round(time.monotonic() - t0, 2),
            "tail": out[-300:] if verdict == "ERROR" else ""}
