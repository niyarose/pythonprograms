# from re import *   # * import all the regular expression 
# text="luminar techno lab luminar techno hub"
# check=finditer("luminar",text)
# count=0
# for c in check:
#     print(c.group()) #print the pattern 
#     print(c.start()) #print the position 
#     count+=1
# print(count)

"""
"""
from re import *
name="aaBCD123$#*"
checker=finditer("[^a-zA-z0-9]",name)
print (checker)
for ch in checker:
    print(ch.group())




"""
[a-z] === /w   [^a-z] === /W
[0-9] === /d   [^0-9] === /D
space === /s   
quantifiers 
a* any number of a 
a{2} 2 times a
a{2,3} minimum 2 maximum 3 
regular expression is used to match pattern 
"""