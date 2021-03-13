#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
echo "Executing App in '$BASEDIR'"
source $BASEDIR/env/bin/activate
python $BASEDIR/main.py

