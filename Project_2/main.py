from random import randint

n = randint(1, 100)

a = -1
guess = 0
while(n != a):
    a = int(input("Enter the no.: "))

    if(a > n):
        print("Too much higher")
    elif(a < n):
        print("Too much lower")
    guess +=1
    
print(f"You choose the no. {n} in {guess} counts")