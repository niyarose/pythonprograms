
# """
# variable declaration rule prgm in java
# """
# from re import *
# varname="num$"
# rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
# matcher=fullmatch(rule,varname)
# # print(matcher)
# if matcher==None:
#     print("Invalid..")
# else:
#     print("Valid..")





#first qs
age=int(input("enter the age: "))
if age<=15:
    print("child")
elif age>=60:
    print("senior citizen")
elif age<=21:
    print("teenager")
else:
    print("adult")

#third qs
lst1=[10,11,13,15]
lst2=[9,8,11,13,14]
list(set(lst1).intersection(lst2))