mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphone14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"],
]
print(len(mobiles),"mobiles available")
#print all mobikes names
mobile_names=[mob[1] for mob in mobiles]
print(mobile_names)
#print 4g mobiles
g_mob=[mob[1] for mob in mobiles if mob[3]=="4g"]
print(g_mob)
#print mobile names price<30000
below_30000=[mob[1] for mob in mobiles if mob[2]<30000]
print(below_30000)
#print mobiles names availoable in range of 30000 to 50000
range=[mob[1] for mob in mobiles if mob[2]>30000 and mob[2]<50000]
print(range)
# range_filter =[mob[1] for mob in mobiles if mob[2] in range(30000,50000)]
# print(range_filter)
five_g=[mob[1] for mob in mobiles if mob[2]<25000 and mob[3]=="5g"]
print(five_g)