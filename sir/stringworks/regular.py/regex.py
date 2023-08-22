# sen="joel is a very good student in my batch"
# words=sen.split(" ")



# # print(sen.startswith("joel"))
# # bol=sen.startswith("joel")
# # print(bol)

# # if bol==True:
# #     print("the sentence is starting with 'joel' ")

# if words[0]=="joel":
#     print("the sentence is starting with 'joel' ")


# import packageName          ^ coret-to check the given string is present in the first position 
import re 
# sen="joel is a very good student in my batch"
# x=re.search("^joel",sen)
# y=re.search("^Joel",sen)
# print(x)
# print(y)
# en=re.search("batch$",sen)
# # $ dollar symbol -to check the given string is present in the last position 
# print(en)

# endstart=re.search("batch$" and "^joel",sen)
# print(endstart)


# st_en1="maharajas is a good college"
# st_en2="maharajas is a good college  "
# nd_st=re.search("^maharajas.*college$",st_en1)
# nd_st2=re.search("^maharajas.*college$",st_en1)
# print(nd_st)
# print(nd_st2)


# import re 
# mob=input("enter your phone number with country code : ")
# print(mob)
# num=re.search("^91",mob)
# print(num)
# if num:
#     print("number is indian number")
# else:
#     print("foreign number")


import re 
mobile=input("enter your phone number with country code : ")
number=re.search("^[+]91",mobile)
print(number)
if number:
    print("the entered number is an indian number .... ")
else:
    print("the entered number is an foreign number .... ")



# resi=input("enter a residential number : ")
# ekm=re.search("^0484",resi)
# tcr=re.search("^0422",resi)
# ijk=re.search("^0426",resi)
# if ekm:
#     print("ekm")
# elif tcr:
#     print("tcr")
# else:
#     print("ijk")








