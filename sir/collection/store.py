items=[
    [1,"potatto",45,"veg",10],
    [2,"tomatto",40,"veg",20],
    [3,"onion",35,"veg",0],
    [4,"brinjal",50,"veg",0],
    [5,"fish",145,"nonveg",10],
    [6,"chicken",145,"nonveg",10],
    [7,"egg",6,"nonveg",100],
]
#total number of products
print(len(items))
#products instock name 
instock_pro=[i[1] for i in items if (i[-1]>0)]
print(instock_pro)
# veg category product name
veg_item=[i[1]for i in items if (i[-2]=="veg")]
print(veg_item) 
# product available in range of 50-60
avail_pro=[i[1] for i in items if i[2] in range(50,60)]
print(avail_pro)
# veg products vailable in 40-80
veg_avail=[i[1] for i in items if i[2] in range(40,80) and i[-2]=="veg"]
print(veg_avail)