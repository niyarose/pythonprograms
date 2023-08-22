party=[]

for i in range(3):
    invites=input( "enter the name :")
    party.append(invites)
    i=i+1
print(party)
more=input("do you what to add another : ")
if more=="yes":
    name=input("enter the name : ")
    party.append(name)
elif more=="no":
    print(f"you have invited {len(party)} persons to the party")
print(party)
    

