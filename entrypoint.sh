#!/bin/sh -l

python3 /app/main.py $1


time=$(python3 /app/main.py $1)
echo "time=$time" >> $GITHUB_OUTPUT

