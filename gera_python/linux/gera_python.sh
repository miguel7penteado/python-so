#!/bin/bash

echo "Executing a bash statement"
export bashvar=100

cat << BLOCO_PYTHON > meu_script_python.py
#!/usr/bin/python
import subprocess

print 'Agora esta sendo executado um script python...'
subprocess.call(["echo","$bashvar"])

BLOCO_PYTHON

chmod 755 meu_script_python.py

meu_script_python.py


