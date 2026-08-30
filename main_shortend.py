#Snake, Water, Gun game

import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1, -1, 0])
youstr = (input("Enter your choice: "))
youdict = {"s": 1, "w": -1, "g": 0}
reversedict ={1: "Snake",-1:"Water",0:"Gun" }

you = youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("Its a Draw!")
else:
    if((computer - you )== -1 or (computer - you) == 2):
        print("You Lose!")
    else:
        print("You Win!")