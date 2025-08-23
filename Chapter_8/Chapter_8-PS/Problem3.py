def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)

number = int(input("Enter a number: "))

print(f"The sum from 1 to {number} is: {sum(number)}")