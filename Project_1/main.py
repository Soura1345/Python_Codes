'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youStr = input("s -> Snake\nw -> Water\ng -> Gun\n\nEnte your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0:"gun"}
you = youDict[youStr]

print(f"Your choice: {reverseDict[you]}\nComputer choice: {reverseDict[computer]}")

if(computer == you):
    print("It's a draw") 
else:
    if(computer == -1 and you == 1):
        print("You Win!") 
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
        