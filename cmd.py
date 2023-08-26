import subprocess
import getpass


inpass = getpass.getpass("Enter the password: ")
apass = "pass123"
if inpass != apass:
  print("Authentication Failure..")
  exit()
cmd = input("Enter your command: ")

x = subprocess.getstatusoutput(cmd)

status = x[0]
output = x[1]

if status == 0:
  print(output)
else:
  print("cmd failure ..")
