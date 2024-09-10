#!/bin/sh -l

python3 /app/main.py $1


time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT




