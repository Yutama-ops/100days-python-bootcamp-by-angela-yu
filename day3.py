print("Welcome to the Treasure Island!\nYour mission is to find the treasure")
direction = (input("What is your height in cm? "))

direction = direction.lower()
if direction == "left":
    print("You can ride the rollercoaster!")
    action = (input("swim or wait"))
    action = action.lower()
    if action == "wait":
        door = (input("wich door? "))
        if door == "yellow":
            print("You win!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")    