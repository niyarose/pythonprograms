# num=0
# if (num<0):
#     print(f"{num} is a negative number")
# elif(num==0):
#     print("number is zero")
# elif (num>0):
#     print(f"{num} is a positive number")


# given number is divisible by 3 print fizz , if number is divisible by 5 print buzz , if number is divisible by 15 print fizzbuzz


# num=int(input("enter a number :"))
# if (num%15==0):
#     print("fizzbuzz")
# elif(num%5==0):
#     print("buzz")
# elif(num%3==0):
#     print("fizz")




#largest number
# num=29
# num1=26
# num3=30
# if ((num>num1)and (num>num3)):
#     print("num is the largest number")
# elif((num1>num3)and(num1>num)):
#     print("num1 is the lagest number ")
# elif((num3>num)and(num3>num1)):
#     print("num3 is largest")


#calculate bmi body mas index
#bmi=weight/height in meter **2

# weight_kg=72
# height_cm=165

# height_meter=height_cm/100
# bmi=weight_kg/height_meter**2
# print(bmi)


num=29
num1=26
num3=30
if ((num>num1)and (num>num3)):
    if(num1>num3):
        print("num1 is 2nd largest")
    else:
        print("num3 is largest")
    print("num is the largest number")
elif((num1>num3)and(num1>num)):
    if(num>num3):
        print("num is 2nd largest")
    else:
        print("num3 is largest")
    print("num1 is the lagest number ")
elif((num3>num)and(num3>num1)):
    if(num>num1):
        print("num is 2nd largest ")
    else:
        print("num1 is 2nd largest")
    print("num3 is largest")
