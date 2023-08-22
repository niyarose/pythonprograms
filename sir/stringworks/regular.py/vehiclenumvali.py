
"""
vehicle number validation
"""
from re import *
num="KL-07-bn-4970"
rule="^KL[-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
matcher=fullmatch(rule,num)
# print(matcher)
if matcher==None:
    print("Invalid..")
else:
    print("Valid..")

