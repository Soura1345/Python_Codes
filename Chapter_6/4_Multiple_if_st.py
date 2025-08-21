age = int(input("Enter your age: "))

if(age % 2 == 0):
    print("Even")


if(age >= 18):
    print("Adult")
elif(age <= 0):
    print("Not valid")
else:
    print("NA")

print("Good bye")