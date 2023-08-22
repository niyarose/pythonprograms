# """
# 1. program to find the common/same elements from the list
# """
# list1=[10,14,15,20,21]
# list2=[8,9,20,21,22]
# (p1,p2)=(0,0) #initial position is 0

# while(p1<len(list1) and p2<len(list2)): #0<4 condition to work from left to right
#     if(list1[p1]==list2[p2]):
#         print(list1[p1])
#         p1+=1
#     elif(list1[p1]<list2[p2]):
#         p1+=1
#     elif(list1[p1]>list2[p2]): #p2=9
#         p2+=1

# """
# 2.list=[1,3,4,6]
# find the least +ve missing integer from the list
# """
# list=[1,3,4,6]

# for i in range(0,len(list)):
#     if list[0]!=1:
#         print(1,"is missing...")
#         break
#     else:
#         elem1=list[i]
#         elem2=list[i+1]
#         if elem2-elem1!=1:
#             print(elem1+1,"is missing...")
#             break

"""
lst=[2,3,4,4,5,5,6,7]
find duplicate element from the list
"""
lst=[2,3,4,4,5,5,6,7]
is_found=False
for i in range(0,len[lst]):
    if lst[i]==lst[i+1]:
        is_found=True
        print(i)
        break


