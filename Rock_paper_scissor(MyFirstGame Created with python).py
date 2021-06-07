# My First Game
import random

# Rock, Paper, Scissor (Game)
def WinGame(computer, You):
    # If two values are equal, declare a tie!
    if computer == You:
        return None

    # Check the possibilities if computer chose Rock(r)
    elif computer == 'r':
        if You =='s':
            return False
        elif You =='p':
            return True
    
    # Check the possibilities if computer chose Paper(p)
    elif computer == 'p':
        if You =='r':
            return False
        elif You =='s':
            return True
    
    # Check the possibilities if computer chose Scissor(s)
    elif computer == 's':
        if You =='p':
            return False
        elif You =='r':
            return True

print("Computer's Turn: Rock(r), Paper(p) or Scissor(s) ?") 
RandNo = random.randint(1, 3) 
if RandNo == 1:
    computer = 'r'
elif RandNo == 2:
    computer = 'p'
elif RandNo == 3:
    computer = 's'

You = input("Your Turn: Rock(r), Paper(p) or Scissor(s) ?")
W = WinGame(computer, You)

print(f"Computer chose {computer}")
print(f"You chose {You}")

if W == None:
    print("The game is a tie !")
elif W:
    print("You Won !")
else:
    print("You Lose !")