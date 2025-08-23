import random

def game():
    print("You are playing:)")
    score = random.randint(1,100)
    
    with open("Text/highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
        
    print(f"Your score is: {score}")
    if(score > highscore):
        with open("Text/highscore.txt", "w") as f:
            f.write(str(score))
    return score

game()