from functools import reduce

l = [11,97,34,678,245,60,125]

def greatest(a,b):
    if(a>b):
        return a
    return b

print(reduce(greatest,l))