#!/bin/bash
touch ~/.qd_path
qd.py "$1" && \
cd "$(cat ~/.qd_path)"
