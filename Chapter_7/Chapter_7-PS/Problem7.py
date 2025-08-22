n = int(input("Enter the num: "))

# for i in range(1, n+1):
#     print(" "* (n-i),end="")
#     print("*"* (2*i-1),end="")
#     print("")

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print("")