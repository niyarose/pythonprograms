"""st={}# empty set
st=set() # creating set"""
#
# st={10,20,"hello","hai",True}
# for el in st:
#     print(el)
#adding an object to set using add()
# st={10,11,25,"hellow",9}
# st.add("hai")
# print(st)
# converting list to set
# lst=[2,3,4]
# st=set(lst)
# print(st)
#union
st1={10,11,12,13}
st2={10,11,12,25,30}
# un_set=st1.union(st2)
# print(un_set)
# intersection
# inter_set=st1.intersection(st2)
# print(inter_set)
#difference
# diff_set=st2.difference(st1)
# print(diff_set)
# lst=[10,20,10,20,12,13,14]
# st=set(lst)
# print(st)
alluser=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_frndlist=["mohanlal","fahad","asif"]
st1=set(alluser)
st2=set(dq_frndlist)
# print(st1)
# print(st2)
diff=st1.difference(st2)
diff.remove("dq")
print("suggestions of dq",diff)
# asif_friendlist=["mohanlal","fahad","vijay","nivin"]
# mutual_friend=set(dq_frndlist).intersection (set(asif_friendlist))
# print("mutual friends : ",mutual_friend)

# word="goodmorning"
# vowel=["a","e","i","o","u","A","E","I","O","U"]
# vowel_count=0
# for ch in word:
#     if ch in vowel:
#         vowel_count+=1
# print(vowel_count)
