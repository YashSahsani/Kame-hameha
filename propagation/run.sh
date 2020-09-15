#!/usr/bin/env bash
# Start server
python3 -m http.server 8000 &> /dev/null &
pid=$!
python3 main.py $pid

