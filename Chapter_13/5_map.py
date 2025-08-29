from functools import reduce

# Map examples
l = [1,2,3,4,5]
square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))

printElement = lambda x:x
print(list(map(printElement,l)))

# Filter example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

odd = lambda n : n%2 != 0
print(list(filter(odd,l)))

# Reduce example
sum = lambda a,b:a+b
print(reduce(sum,l))

mul = lambda a,b:a*b
print(reduce(mul,l))