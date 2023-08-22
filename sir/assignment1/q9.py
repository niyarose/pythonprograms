num=int(input("enter how many people:"))
if num<10:
    people=[]
    print("enter the names of people:")
    for i in range(num):
        name=input()
        people.append(name)
        for n in people:
            print(n,"has been invited")
elif num>=10:
    print("too many people")