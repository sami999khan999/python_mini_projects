from controllers import (
    add_books,
)  # Import necessary functions for handling books.


# Define the 'insert_books' function to add books to the database.
def insert_books():
    try:
        # Start a loop that allows the user to insert multiple books.
        while True:
            # Prompt the user to enter the book title and content.
            title = input("Enter the title of the book: ")
            content = input("Enter the content of the book: ")

            # Add the book to the database using 'add_books' and store the result.
            res = add_books(title, content)

            # If the result is positive, the book was added successfully.
            if res:
                print(f"Book '{title}' added successfully!")
            else:
                # If the result is 0 or negative, there was an error while adding the book.
                print(f"Cannot add book '{title}'!")

            # Ask the user if they want to add another book or exit the insertion process.
            choice = input(
                "Press `y` if you would like to add another book or press `exit` to exit: "
            ).lower()

            # If the user wants to add another book, continue the loop.
            if choice == "y":
                continue

            # If the user enters 'exit', break the loop and end the function.
            elif choice == "exit":
                break

            # If the user input is invalid, raise a ValueError.
            else:
                raise ValueError("Enter a valid option.")

    # Handle invalid user input (e.g., entering something other than 'y' or 'exit').
    except ValueError as ve:
        print(ve)

    # Handle any unexpected errors during the book insertion process.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
