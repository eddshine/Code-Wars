
# MY CODE
# def zero(num=None): #your code here
#     if num==None:
#         return 0
#     else:
#         if num[0]=="+":
#             return 0 + num[1]
#         elif num[0]=="-":
#             return 0 - num[1]
#         elif num[0]=="*":
#             return 0 * num[1]
#         else:
#             return int(0 / num[1])
# def one(num=None): #your code here
#         if num==None:
#             return 1
#         else:
#             if num[0]=="+":
#                 return 1 + num[1]
#             elif num[0]=="-":
#                 return 1 - num[1]
#             elif num[0]=="*":
#                 return 1 * num[1]
#             else:
#                 return int(1 / num[1])
# def two(num=None): #your code here
#         if num==None:
#             return 2
#         else:
#             if num[0]=="+":
#                 return 2 + num[1]
#             elif num[0]=="-":
#                 return 2 - num[1]
#             elif num[0]=="*":
#                 return 2 * num[1]
#             else:
#                 return int(2 / num[1])
# def three(num=None): #your code here
#         if num==None:
#             return 3
#         else:
#             if num[0]=="+":
#                 return 3 + num[1]
#             elif num[0]=="-":
#                 return 3 - num[1]
#             elif num[0]=="*":
#                 return 3 * num[1]
#             else:
#                 return int(3 / num[1])
# def four(num=None): #your code here
#         if num==None:
#             return 4
#         else:
#             if num[0]=="+":
#                 return 4 + num[1]
#             elif num[0]=="-":
#                 return 4 - num[1]
#             elif num[0]=="*":
#                 return 4 * num[1]
#             else:
#                 return int(4 / num[1])
# def five(num=None): #your code here
#         if num==None:
#             return 5
#         else:
#             if num[0]=="+":
#                 return 5 + num[1]
#             elif num[0]=="-":
#                 return 5 - num[1]
#             elif num[0]=="*":
#                 return 5 * num[1]
#             else:
#                 return int(5 / num[1])
# def six(num=None): #your code here
#         if num==None:
#             return 6
#         else:
#             if num[0]=="+":
#                 return 6 + num[1]
#             elif num[0]=="-":
#                 return 6 - num[1]
#             elif num[0]=="*":
#                 return 6 * num[1]
#             else:
#                 return int(6 / num[1])
# def seven(num=None): #your code here
#         if num==None:
#             return 7
#         else:
#             if num[0]=="+":
#                 return 7 + num[1]
#             elif num[0]=="-":
#                 return 7 - num[1]
#             elif num[0]=="*":
#                 return 7 * num[1]
#             else:
#                 return int(7 / num[1])
# def eight(num=None): #your code here
#         if num==None:
#             return 8
#         else:
#             if num[0]=="+":
#                 return 8 + num[1]
#             elif num[0]=="-":
#                 return 8 - num[1]
#             elif num[0]=="*":
#                 return 8 * num[1]
#             else:
#                 return int(8 / num[1])
# def nine(num=None): #your code here
#         if num==None:
#             return 9
#         else:
#             if num[0]=="+":
#                 return 9 + num[1]
#             elif num[0]=="-":
#                 return 9 - num[1]
#             elif num[0]=="*":
#                 return 9 * num[1]
#             else:
#                 return int(9 / num[1])

# def plus(num=None): #your code here
#     return ['+',num]
# def minus(num=None): #your code here
#     return ['-', num]
# def times(num=None): #your code here
#     return ['*', num]
# def divided_by(num=None): #your code here
#     return ['/', num]

# print(three(divided_by(two())))
# print(four(plus(nine())), 13)
# print(eight(minus(three())), 5)
# print(six(divided_by(two())), 3)




#======================= BETTER WRITTEN CODE BY SOMEONE ================================================================================

# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y // x

# print(three(divided_by(two())))
# print(four(plus(nine())), 13)
# print(eight(minus(three())), 5)
# print(six(divided_by(two())), 3)
