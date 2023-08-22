# lst=[
#     [1,2],
#     [4,50],
#     [50,45],
# ]
# """
# print all list
# """
# for i in lst:
#     print(i)
# for ls in lst:
#     for num in ls:
#         print(num)

"""
print all numbers > 5
"""
# lst=[
#     [1,2],
#     [4,50],
#     [50,45],
# ]
# for ls in lst:
#     for num in ls:
#         if (num > 5):
#             print(num)
# #print all numbers
# allnumbers=[num for ls in lst for num in ls ]
# print(allnumbers)
# #print number>5
# gt_five=[num for ls in lst for num in ls if num>5 ]
# print(gt_five)