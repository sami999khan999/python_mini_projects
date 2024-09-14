import random


def guess():
    try:
        random_number = random.randint(1, 100)
        attempts = 0
        print("Welcome to the Number Guessing Game!")

        while True:
            guess = int(input("Inter a number between 1 and 100: "))

            if guess < 1 or guess > 100:
                print("Error: Please enter a number between 1 and 100.")
                continue

            if guess > random_number:
                attempts += 1
                print("Too high")
                print(attempts)
            elif guess < random_number:
                attempts += 1
                print("Too low")
                print(attempts)
            else:
                attempts += 1
                print("Current guess")
                break

    except ValueError as ve:
        print("Invalid input. Please enter a valid integer.")


guess()
