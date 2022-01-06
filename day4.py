# 🚨 Don't change the code below 👇
import random
rock = ["rock", "peper", "scissor"]


your_choice = int(input("whats your choice: 0 for rock, 1 for pepper, 2 for scissors "))
comp_choice = random.randint(0, 2)

if rock[your_choice] == 0 and rock[comp_choice] == 1:
    print(comp_choice)
    print("you lost")
elif  rock[your_choice] == 1 and rock[comp_choice] == 2:
    print(comp_choice)
    print("you lost")
elif rock[your_choice] == rock[comp_choice]:
    print(comp_choice)
    print("its a draw")
else:
    print(comp_choice)
    print("You win")

