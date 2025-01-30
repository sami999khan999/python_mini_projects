import random


def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll


while True:
    player = input("Enter the number of players (2-4): ")

    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Invalid number of players. Please enter a number between 2 and 4.")

max_score = 50
player_scores = [0 for _ in range(player)]


while max(player_scores) < max_score:
    for player_idx in range(player):
        print(f"\nPlayer {player_idx + 1}'s turn")
        print(f"Your total score is {player_scores[player_idx]} \n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll the dice? (y/n): ")

            if should_roll.lower() != "y":
                break

            roll_value = roll()

            if roll_value == 1:
                current_score = 0
                print("You rolled a 1. Your turn is over. \n")
                break
            else:
                current_score += roll_value
                print(
                    f"You rolled a {roll_value}. Your current score is {current_score} \n"
                )

                if (
                    current_score >= max_score
                    or player_scores[player_idx] + current_score >= max_score
                ):
                    print(
                        f"Congratulations! Player {player_idx + 1} has reached or surpassed the maximum score of {max_score} \n"
                    )
                    break

        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f"Player {winning_idx + 1} wins with a score of {max_score}")
