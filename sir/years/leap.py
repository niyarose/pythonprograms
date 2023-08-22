fread=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\years\\data.txt","r") #read from the data.txt 
fwrite=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\years\\leapyr.txt","w") #automatically create new txt file and write into it

for yr in fread:
    years=int(yr.rstrip("\n"))
    if (years%100==0 and years%400==0):
        fwrite.write(str(yr))
    elif (years%100!=0 and years%4==0):
        fwrite.write(str(yr))
print("processed")

