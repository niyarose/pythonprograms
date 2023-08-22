year=1900
#year % 4==0 leapyear   year%400==0 leapyear year%100!=0


# is_leapyear=False
# if(year%4==0):
#     is_leapyear=True
# elif(year%400==0):
#     is_leapyear=True
# elif(year%100!=0):
#     is_leapyear=False
# print(year,"is a leapyear",is_leapyear)

if (year%4==0 and year%100!=0 or year%400==0):
    print(year,"is a leapyear")
else:
    print(year,"is not a leapyear")