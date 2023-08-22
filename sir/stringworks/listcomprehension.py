lst=[3,4,5,6,7]
odds=[num for num in lst if num %2!=0] #return value|iteration|condition
print(odds)
even=[num for num in lst if num %2==0]
print(even)
num_gt_five=[num for num in lst if num >5]
print(num_gt_five)
cubes=[num**3 for num in lst ]
print(cubes)
"""
print all numbers divisible by 3
"""
lst=[3,4,5,6,7]
mult=[num for num in lst if num%3==0]
print(mult)