from re import *

f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\email\\data.txt","r")
validate_email=set()
rules="[a-zA-Z0-9][a-zA-Z0-9_$#]*[@]gmail[.]com"
for id in f:
    id=id.rstrip("\n")
    matcher=fullmatch(rules,id)
    if matcher!=None:
        validate_email.add(id)
print(validate_email)