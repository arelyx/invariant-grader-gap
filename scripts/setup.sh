#!/bin/bash
# Fetch the external tools into third_party/ and create the Python environment.
# UAutomizer needs Java 21. ESBMC ships as a static binary.
set -e
cd "$(dirname "$0")/.."
mkdir -p third_party && cd third_party
[ -d wonda ] || git clone https://github.com/idopinto/wonda.git
if [ ! -d esbmc ]; then
  curl -L -o esbmc-linux.zip https://github.com/esbmc/esbmc/releases/download/v8.6/esbmc-linux.zip
  unzip -q esbmc-linux.zip -d esbmc && rm esbmc-linux.zip && chmod +x esbmc/release/bin/esbmc
fi
if [ ! -d uautomizer ]; then
  # SV-COMP 2025 release of Ultimate Automizer (0.3.0-dev-d790fec)
  curl -L -o uautomizer.zip https://zenodo.org/api/records/14209043/files/uautomizer.zip/content
  mkdir uautomizer && unzip -q uautomizer.zip -d uautomizer && rm uautomizer.zip
fi
cd ..
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q pycparser psutil matplotlib -r third_party/wonda/requirements.txt 2>/dev/null \
  || .venv/bin/pip install -q pycparser psutil matplotlib
echo "done. Check src/paths.py if the tool folders differ."
