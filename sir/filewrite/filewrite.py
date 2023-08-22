# f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\filewrite\\data.txt","w")
# f.write("python programming")
# print("process file=updated")



f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\filewrite\\data.txt","w")
language=["python" , "java " ," c++" , "c programming"]

for l in language:
    # print(l)
    f.write(l+"\n")
print("processed")
f.close()