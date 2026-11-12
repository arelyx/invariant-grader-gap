"""Full grader: Ultimate Automizer (UAutomizer), an unbounded software verifier.

Verdicts come straight from the tool: TRUE (property proved for all executions),
FALSE (a real violating execution exists), UNKNOWN, TIMEOUT, ERROR.
Only TRUE and FALSE are definite answers.
"""
import os
import re
import shutil
import signal
import subprocess
import tempfile
import time

import paths

RESULT_RE = re.compile(r"Result:\s*\n(ERROR|TRUE|FALSE|UNKNOWN)(?::\s*(.+))?", re.M)


def run_uautomizer(c_code: str, timeout: float = 120.0) -> dict:
    os.makedirs(paths.TMP, exist_ok=True)
    wd = tempfile.mkdtemp(prefix="ua_", dir=paths.TMP)
    src = os.path.join(wd, "prog.c")
    with open(src, "w") as f:
        f.write(c_code)
    cmd = ["python3", str(paths.ULTIMATE), "--spec", str(paths.PRP), "--architecture", "32bit",
           "--file", src, "--full-output", "--witness-dir", wd, "--witness-name", "w"]
    env = os.environ.copy()
    env["PATH"] = str(paths.ULTIMATE.parent) + os.pathsep + env.get("PATH", "")
    t0 = time.monotonic()
    p = subprocess.Popen(cmd, cwd=wd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, start_new_session=True)
    try:
        out, _ = p.communicate(timeout=timeout)
        m = RESULT_RE.search(out)
        decision = m.group(1) if m else "ERROR"
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)   # kills the Java child too
        p.wait()
        decision = "TIMEOUT"
    shutil.rmtree(wd, ignore_errors=True)
    return {"decision": decision, "seconds": round(time.monotonic() - t0, 2)}
