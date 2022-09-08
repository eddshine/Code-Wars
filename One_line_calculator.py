# RULES
# 1.No using loop.
# 2.No using conditional statements.

# Take all inputs from the users.
# Take 9 random arithmetic symbols.
randOperators = list(input('Enter 9 random arithmetic op: '))

#Take 10 random numbers separated by semi-colon(;).
randNumbers = input('Enter 10 random values separated by ";": ').split(';')

# Create an empty list with a size of s=s*(list1 + list2)
result = [None]*(len(list(randNumbers))+len(randOperators))

# Append list_1 and list_2 in alternating order.
result[::2] = list(randNumbers)
result[1::2] = randOperators
# Joining all chars into one string
result = ''.join(result)

# Do all calculations using eval and printing the result after that.
print(f"The result of {result} is {eval(result)}")

