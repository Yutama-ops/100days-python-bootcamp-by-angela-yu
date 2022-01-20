import random
number = random.randrange(100)
print("Welcome to guessing number game.")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Print choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
else:
    attempt = 5
print(f"You have {attempt} attempts remaining to guess the number")

def guess_number():
    guess_number = int(input("Make a guess: "))
    if guess_number != number:
        if guess_number > number:
            print("Too High")
            return False
        else:
            print("Too Low")
            return False
    else:
        return True
print(number)
while attempt > 0 and guess_number() == False:
    print(f"You have {attempt} attempts remaining to guess the number")
    game_stat = guess_number()
    print(game_stat)
    attempt -= 1
    if not game_stat:
        print("guess again.")


