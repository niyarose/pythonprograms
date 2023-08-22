
from json import load 
with open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\moviedb\\mdb.json","r",encoding="UTF-8") as f:
    data=load(f)
# #total number of movies
# print(len(data))

#print all movie names 
# names=[u.get("title") for u in data]
# print(names)




#print movie with highest duration 
# duration=max(data,key=lambda m:int(m.get("runtime")))
# print(duration.get("title"))


#print all genres 
#print movie name which contains genres comedy 
#print movie name which conatin genres comedy or fantasy 
# year wise movie count (1988:5,1984:3)

# all_genres={g for u in data for g in u.get("genres")}
# print(all_genres)
comedy_genres=[u.get("title") for u in data if "Fantancy" in u.get("genres")]
print(comedy_genres)


# for u in data:
#     if u.get("genres")=="comedy":
#         print(u.get("title"))

# fc_genres=[u.get("title") for u in data if u.get("genres")=="comedy" or u.get("genres")=="fantasy"]
# print(fc_genres)