a = int(input("Enter 1st np.: "))
b = int(input("Enter 2nd no.: "))

if(b == 0):
    raise ZeroDivisionError("Can't be divisible")
else:
    print(f"The division of a/b is {a/b}")