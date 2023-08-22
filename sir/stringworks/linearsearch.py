#linear searching
lst=[1,2,5,6,8,9]
element=int(input("enter the number to search : "))
is_found= False
for i in range(0,len(lst)):
    if element==lst[i]:
        is_found= True
        break
print("found" if is_found == True else "not found")
