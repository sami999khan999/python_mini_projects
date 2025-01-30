import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERANDE = 3
MAX_OPERANDE = 15
TOTAL_ROUNDS = 5


def generate_problem():
    left_operand = random.randint(MIN_OPERANDE, MAX_OPERANDE)
    right_operand = random.randint(MIN_OPERANDE, MAX_OPERANDE)
    operator = random.choice(OPERATORS)

    expression = f"{left_operand} {operator} {right_operand}"
    answer = eval(expression)

    return expression, answer


wront = 0
input("Press any button to start!")
print("==========================")

start_time = time.time()


for i in range(TOTAL_ROUNDS):
    exp, ans = generate_problem()

    while True:
        player_answer = input(f"Round #{i + 1}: {exp} = ")

        if player_answer == str(ans):
            break
        wront += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
