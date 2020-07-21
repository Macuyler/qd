#!/bin/bash
touch ~/.qd_path
qd.py $@ && \
cd "$(cat ~/.qd_path)"
