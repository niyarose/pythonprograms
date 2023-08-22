#print sum of digits of given number 
num=123
sum=0
while(num!=0):
    digit=num%10
    num=num//10
    sum+=digit
print("the sum of the given  digit is",sum)