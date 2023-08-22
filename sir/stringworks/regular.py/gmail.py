# #gmail verification 
# import re 
# gmail=input("enter your gmail id : ")
# g=re.search("@gmail.com$",gmail)
# if g:
#     print("the entered gmail is valid...")
# else:
#     print("the entered gmail is not valid...")


# import re

# rule = "[K][L]{2}[-][0-9]{2}[-][a-z]{2}[0-9]{4}"
# number = "KL-08-bn-4970"
# matcher = re.fullmatch(rule, number)

# if matcher is None:
#     print("invalid..")
# else:
#     print("valid...")


import re

rule = r"[K][-][L]{2}[-][0-9]{2}[-][a-z]{2}[0-9]{4}"
number = "KL-08-bn-4970".strip()  # Remove leading/trailing whitespace
matcher = re.fullmatch(rule, number)

if matcher is None:
    print("invalid..")
else:
    print("valid...")
