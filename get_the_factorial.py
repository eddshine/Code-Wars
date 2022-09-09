from functools import reduce
num = int(input('Enter number: '))
def factorial(n):
    return reduce(lambda x,y: x*y,[x for x in reversed(range(num, 0, -1))])
print(f'Factorial: {factorial(num)}')
