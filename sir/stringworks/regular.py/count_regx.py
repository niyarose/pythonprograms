# import re 
# sent="hi hello hi hello good afternoon hello hi hide"
# # ct=sent.count("hi")
# print(ct) 
# # or 
# cl=re.findall("hi",sent)
# print(cl)
# print(len(cl))

# """
# """
import re
sent1="hi hello hi hello 13 good afternoon hello hi hide 11:13 15 78"
num=re.findall("[0-5][0-9]",sent1)
print(num)



