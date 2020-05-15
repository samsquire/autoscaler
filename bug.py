#!/usr/bin/env python3
import sys
from subprocess import Popen, PIPE

watcher = Popen(["bash", "-c", "top -b | grep --line-buffered Cpu"], stdout=PIPE)

while True:
    line = watcher.stdout.readline()
    print(line.decode('utf8').rstrip())
