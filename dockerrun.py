#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess as sp
# osname = input("Enter your os name:")
# image = input("Name of the base image: ")


form = cgi.FieldStorage()
osname = form.getvalue("x")
image = form.getvalue("y")

cmd  = "sudo docker run -dit --name {} {}".format(osname, image)
result = sp.getstatusoutput(cmd)
status = result[0]
output = result[1]

# print(status)
#gedprint(osname)
if status == 0:
  print("os launched named {} ...".format(osname))
else:
  print("some error: {}".format(output))
