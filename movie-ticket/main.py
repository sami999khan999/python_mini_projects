def price_by_age(age):
    if age <= 10:
        return 300
    elif 11 <= age <= 25:
        return 500
    elif 26 <= age <= 60:
        return 500
    else:
        return 400


try:
    age = int(input("Age: "))

    if age <= 0:
        raise ValueError("Invalid input. Age must be a positive number.")

    price = price_by_age(age)

    time = input("ShowTime (HHMM): ")

    if len(time) != 4 or not time.isdigit():
        raise ValueError("Invalid input. Show time must be in HHMM format.")

    final_discount = 0
    final_price = price

    if int(time) <= 1700:
        discount = 10
        final_discount = (price / 100) * discount
        final_price = price - final_discount

    print(f"Ticket Price: {price} BDT")
    print(f"Discount: {final_discount} BDT")
    print(f"Final Price: {final_price} BDT")

except ValueError as e:
    print(e)
except Exception:
    print("An error occurred")
