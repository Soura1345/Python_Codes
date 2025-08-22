def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(f"The greatest of three no is : {greatest(a,b,c)}")