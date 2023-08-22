# import re 
# text="abababab"
# text1="aaaabbbcccc"
# t=re.search("[a]{4}",text)
# t1=re.search("[a]{4}",text1)
# print(t)
# print(t1)


# import re 
# text1="abcdeeefgghhhhhijkl"
# t=re.search("[a-z]{4}",text1) #{} for indicating position 
# print(t)


#homework...mobile number verification 




import re 
text1="123abCDEFeeefgghhhhhijkl"
t=re.search("[a-z]{2}[A-Z]{4}",text1) #if the position chance it will return false "aaabDCFEmmdk"
print(t)


