def factorial(n):
    if( n==0 or n==1):
        return n
    else:
        return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"the factorial of {n} is {factorial(n)}")
