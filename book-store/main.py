from read_books import (
    read_books,
)  # Import the 'read_books' function from the read_books module.
from insert_books import (
    insert_books,
)  # Import the 'insert_books' function from the insert_books module.
from delete_book import (
    delete_book,
)  # Import the 'delete_book' function from the delete_book module.


def library():
    # This is the main function that runs the library system.
    # It displays a menu for the user to choose actions (read, insert, delete books).
    # The loop continues until the user chooses to exit.

    while True:  # Infinite loop to keep the program running until the user exits.
        try:
            # Display a menu with options for the user.
            print("=============== Welcome to the library! ============")
            print("Press 1 to read a book")  # Option to read a book.
            print("Press 2 to insert a book")  # Option to insert a new book.
            print("Press 3 to delete a book")  # Option to delete a book.
            print(
                "Enter 'exit' to exit the library"
            )  # Option to exit the library system.
            print("=====================================================")

            # Get the user's input for the action they want to perform.
            action = input("Enter your choice: ")

            # Validate the user's input. If it doesn't match any of the expected choices, raise an error.
            if action not in ("1", "2", "3", "exit"):
                raise ValueError(
                    "Invalid action. Please choose between 1, 2, and 3."
                )  # Raise a ValueError if input is invalid.

            # If the user chooses to exit, break the loop and end the program.
            if action == "exit":
                break

            # Handle reading a book.
            if action == "1":
                read_books()  # Call the 'read_books' function to display book content.

            # Handle inserting a new book.
            if action == "2":
                insert_books()  # Call the 'insert_books' function to add a new book to the database.

            # Handle deleting an existing book.
            if action == "3":
                delete_book()  # Call the 'delete_book' function to remove a book from the database.

        except ValueError as ve:
            # If there was an invalid input (wrong choice), catch the ValueError and display a friendly message.
            print(ve)

        except Exception as e:
            # Catch any other unexpected exceptions and display the error message.
            print(e)


# Call the library function to start the library system when the script is run.
library()
