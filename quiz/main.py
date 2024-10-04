from data import quiz_data as data

score = 0

for d in data:
    print(d["question"])
    for options in d["options"]:
        print(options)

    answer = input("Enter the correct option (A, B, C, D)? ").upper()

    if answer == "EXIT":
        break

    if answer not in ["A", "B", "C", "D"]:
        print("Invalid Option!")
        continue

    if any(option.startswith(answer) for option in d["options"]) and d[
        "answer"
    ].startswith(answer):
        score += 1
        print("Currect answer, score: ", +int(score))
    else:
        print(f"Wrong! The correct answer was: {d['answer']}")
    print()

print("Final Score: ", score)
