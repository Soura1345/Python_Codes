def div5(n):
    if(n%5==0):
        return True
    return False

a = [34,678,2345,67890,12345]

f = (list(filter(div5,a)))
print(f)