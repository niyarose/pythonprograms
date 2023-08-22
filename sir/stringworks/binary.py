#binary searching
lst=[1,2,4,5,6,7]
low=0
upp=len(lst)-1
element=int(input("enter the number to search : "))
is_found= False
while(low<=upp):
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found= True
        break
    elif element>lst[mid]:
            low=mid+1
    elif element<lst[mid]:
        upp=mid-1
print("the number is found..." if is_found==True else "the number is not found...")

