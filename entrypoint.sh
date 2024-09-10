#!/bin/sh -l

python3 /app/main.py $1


pokemon=$(python3 /app/main.py $1)
echo "pokemon=$pokemon" >> $GITHUB_OUTPUT



