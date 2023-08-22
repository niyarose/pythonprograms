from json import load 
with open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\jsonprocess\\data.json","r") as f:
    data=load(f)


# for u in data:
    # print(u.get("name"))


# names=[u.get("name") for u in data]
# print(names)


#student with highest marks
# candidate=max(data,key=lambda s:s.get("total"))
# print(candidate)

# #sort all students wrt total marks order by descending 
# out=sorted(data,reverse=True,key=lambda s:s.get("total"))
# print(out)


stream=[u.get("name") for u in data if u.get("course")=="bca"]
print(stream)