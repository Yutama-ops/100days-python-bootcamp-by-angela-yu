import random
from art import logo
from art import vs
from game_data import data

score = 0
choice1 = random.choice(data)
choice2 = random.choice(data)
game = True
print(logo)

while game:
    while choice1 == choice2:
        choice2 = random.choice(data)
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B' ")

    if user_choice == 'A':
        if choice1["follower_count"] > choice2["follower_count"]:
            choice2 = random.choice(data)
            score += 1
        else:
            game = False
            print(score)
    elif user_choice == 'B':
        if choice1["follower_count"] < choice2["follower_count"]:
            choice1 = choice2
            choice2 = random.choice(data)
            score += 1
        else:
            game = False
            print(score)

