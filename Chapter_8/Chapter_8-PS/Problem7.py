def multiply(n):
    i = 1
    while(i<=10):
        print(f"{n} X {i} = {n*i}")
        i +=1

num = int(input("Enter the table for: "))

multiply(num)