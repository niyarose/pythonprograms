""""
variable declaration rule prgm in python

"""
from re import *
varname="num_12"
rule="[a-zA-Z_][a-zA-Z0-9_]*"
matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid..")
else:
    print("valid")

""""
variable declaration rule prgm in java

"""
from re import *
varname="num$"
rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
matcher=fullmatch(rule,varname)
# print(matcher)
if matcher==None:
    print("Invalid..")
else:
    print("Valid..")


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