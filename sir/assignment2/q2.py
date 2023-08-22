party=["Niya","Neenu","Beksy","Joy"]
sel_name=input("enter the name : ")

if sel_name in party:
    print(party.index(sel_name))
    
else: 
    print("invalid")  
name=input("do you still want this person to come to the party : ")
if name=="yes":
    print("invited...")
elif name=="no":
    party.remove(sel_name)
    print(party)
else:
    print("invalid entry..")
    