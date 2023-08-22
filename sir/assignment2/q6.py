dic={
    "book1":{"book":"the guide","author":"narayanan","publication_year":1958,"genre":"classic"},
    "book2":{"book":"eraly india","author":"romila thapar","publication_year":1300,"genre":"History"},
    "book3":{"book":"sacred games","author":"sartaj singh","publication_year":2006,"genre":"thriller and mystery"},
    "book4":{"book":"those pricey thakur girls","author":"anuja chauhan","publication_year":1988,"genre":"romance"} 
    }

# new=dic["book1"]["book"]= "k.r.narayanan"
# print(new)
dic ["book4"]={"book":"dork trilogy","author":"robin einstein","publication_year":1945,"genre":"comedy"}
print(dic)
year=input("enter the year to check : ")
for i in dic:
    for j in dic:
        if year<j["publication_year"]:
            print("publication_year")