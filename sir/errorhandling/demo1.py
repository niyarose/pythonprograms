lst=[10,20,30,40,50]

location=int(input("enter the location to fetch value from list : "))

try:
    print(lst[location])


except Exception as e:
    print(e.args)
    location=int(input("enter the location to fetch value from list : "))
    print(lst[location])


finally:
    print("commit1")
    print("file read")