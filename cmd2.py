import subprocess
#subprocess.getstatusoutput("date")
x = subprocess.getstatusoutput("date")
print(x) 

# getstatusoutput returns the output not prints..
# that is why we need to store the ourtput of the command in a variable x 
#and then print the output..

otherwise 
# subprocess.getstatusoutput("date") this statement won't print the output of date command
