# (Project 1) : Simple Calculator


# OVERVIEW:
# In this assignment, you will develop a basic calculator program using Python. This project
# will reinforce fundamental programming concepts including functions, user input,
# conditional statements, and error handling. The application will run in the terminal and
# should not use any external libraries or frameworks.


# TASKS:
# Function Definitions: Implement functions for the following operations: addition,
# subtraction, multiplication, division, and modulus. Each function should take two
# arguments, perform the corresponding operation, and return the result.
# Implement User Input Handling: Prompt the user to select an operation( e.g. 1
# for Add, 2 for Subtract, 3 for Multiply, 4 for Divide and 5 for Modulus) and input two
# numbers. Convert these inputs into appropriate data types for calculations.
# Conditional Logic: Use ‘if’, ‘elif’, and ‘else’ statements to determine which
# arithmetic operation to perform based on user selection.
# Output Formatting: Display the results in a clear and readable format. Examples:
# Addition: 5 + 6 = 11
# Division: 5 / 2 = 2.50
# Error Handling: Include checks to handle division by zero and other potential
# errors. Provide informative error messages to guide the user.


# SAMPLE INPUT OUTPUT:
# Select operation:
# Add
# Subtract
# Multiply
# Divide
# Modulus
# Enter choice (1/2/3/4/5): 1
# Enter first number: 5
# Enter second number: 8
# 5.0 + 8.0 = 13.0


def calculator():
    try:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        operator = float(input("Enter choice (1/2/3/4/5): "))

        if operator not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid operator. Please choose between 1 and 5.")

        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if operator == 1:
            print(f"{n1} + {n2} = {n1 + n2}")
        elif operator == 2:
            print(f"{n1} - {n2} = {n1 - n2}")
        elif operator == 3:
            print(f"{n1} * {n2} = {n1 * n2}")
        elif operator == 4:
            if n2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            print(f"{n1} / {n2} = {n1 / n2}")
        elif operator == 5:
            print(f"{n1} % {n2} = {n1 % n2}")

    except ValueError as ve:
        print(f"Input error: {ve}")

    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


calculator()
