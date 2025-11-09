import random

while True:
    user_input = input("Would you like to roll the dice? y/n: ").lower()

    if user_input == "y":
        roll_one = random.randint(1, 6)
        roll_two = random.randint(1, 6)
        print(f"You rolled: {roll_one} and {roll_two}")
    elif user_input == "n":
        print("thanks for playing!")
        break
    else:
        print("Please type 'y' or 'n' .\n")
