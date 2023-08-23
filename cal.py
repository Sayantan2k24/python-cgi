#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
cmd = subprocess.getoutput("cal")
print(cmd)
