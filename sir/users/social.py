f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\users\\data.txt","r")
for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",") 
    print(name, followers,followings)