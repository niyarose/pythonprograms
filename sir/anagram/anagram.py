string1=input("enter a string :")
string2=input("enter a string :")
# if(len(string1)==len(string2)):
#     sorted_str1=sorted(string1)
#     sorted_str2=sorted(string2)
# if(sorted_str1==sorted_str2):
#     print(string1 , "and" , string2 ," are anagram ")
# else:
#     print("not anagram"

sorted_str1=sorted(string1)
sorted_str2=sorted(string2)
print("anagram " if sorted_str1==sorted_str2 else "not anagram")

