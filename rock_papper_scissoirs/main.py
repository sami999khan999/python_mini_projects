import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper, Scissors? :").lower()

    if player not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    if player == computer:
        print("Player " + player)
        print("Computer " + computer)
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("Player " + player)
        print("Computer " + computer)
        print("You won!")
    else:
        print("Player " + player)
        print("Computer " + computer)
        print("You lost!")

    continue_or_not = input("Do you want to continue? ").lower()
    if continue_or_not == "no":
        print("Thanks for playing!")
        break
