import random


def guess(n):
    random_number = random.randint(1, n)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 0 and {n}: "))

        if guess < random_number:
            print("Too low, Try again.")
        elif guess > random_number:
            print("Too high, Try again.")
    print(f"You have gurssed the number {random_number} currectly!")


guess(10)
