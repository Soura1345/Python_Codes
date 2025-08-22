n = int(input("Enter the number: "))

fac = 1

for i in range(1, n+1):
    fac *= i

print(f"The factorial of {n} is {fac}")