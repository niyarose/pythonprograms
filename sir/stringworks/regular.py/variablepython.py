"""
variable declaration rule prgm in python
"""
from re import *
varname="num_1"
rule="[a-zA-Z_][a-zA-Z0-9_]*"
matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid..")
else:
    print("valid..")