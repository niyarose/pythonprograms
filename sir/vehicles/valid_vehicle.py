from re import *

f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\vehicles\\data.txt","r")
valid_tn_number=set()
valid_kl_number=set()
rule1="[K][L][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
rule2="[T][N][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
for n in f:
    vehicle_num=n.rstrip("\n")
    matcher=fullmatch(rule1,vehicle_num)
    matcher2=fullmatch(rule2,vehicle_num)
    if matcher!=None:
        valid_kl_number.add(vehicle_num)
    if matcher2!=None:
        valid_tn_number.add(vehicle_num)


print(valid_kl_number)
print(valid_tn_number)

