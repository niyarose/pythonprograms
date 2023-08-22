# f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\FILEIO\\data.txt","r")
# for line in f: #line="hello hai\n"
#     print(line.rstrip("\n"))

# print("line1\n")
# print("line2")


f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\FILEIO\\data.txt","r")
words=[]
for line in f:
    #line="hello hai\n"
    line=line.rstrip("\n")
    text=line.split(" ") #w=[hello,hai]
    for w in text:
        words.append(w)
print(words)



# """
# or
# """

# f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\FILEIO\\data.txt","r")
# words=[]
# for line in f:
#     #line="hello hai\n"
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         words.append(w)
# print(words)

"""

 remove duplicate items 

# """
# f=open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\FILEIO\\data.txt","r")
# words=set()
# for line in f:
#     #line="hello hai\n"
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         words.add(w)
# print(words)




# lstrip(): remove any leftside character 
# rstrip(): remove any rightside character



# data="hello hai\n"
# data.rstrip("\n")




