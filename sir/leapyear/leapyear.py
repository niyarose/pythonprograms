f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\leapyear\\data.txt","w")
years=[2000,2024,1991,1995,1200,1400,1234]
for l in years:
    if (l % 100==0 and l % 400==0):
        f.write(str(l)+"\n")
    elif (l%100!=0 and l%4==0):
        f.write(str(l)+"\n")
print("processed") 
