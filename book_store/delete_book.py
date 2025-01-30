from controllers import (
    get_titles,
    delete_book as delete_from_db,
)  # Import necessary functions from controllers.


# Define the 'delete_book' function to handle the deletion of books from the database.
def delete_book():
    while True:
        try:
            # Fetch the list of book titles from the database using 'get_titles()'.
            titles = get_titles()

            # If there are no books available, print a message and return to end the function.
            if not titles:
                print("No books available to delete.")
                return

            # Display all the available books by their corresponding number.
            for idx, (title,) in enumerate(titles):
                print(f"{idx + 1}: {title}")

            # Ask the user to select the number of the book they want to delete or exit the process.
            user_input = input(
                "Enter a number corresponding to the book you want to delete or 'exit' to exit: "
            )

            # If the user enters 'exit', return to exit the function.
            if user_input.lower() == "exit":
                return

            # Convert the user's input to an integer (assuming the input is a number).
            choice = int(user_input)

            # Validate if the choice is within the range of available book numbers.
            if choice < 1 or choice > len(titles):
                raise ValueError("Invalid choice!")  # Raise an error for invalid input.

            # Get the title of the book to delete based on the user's choice.
            title_to_delete = titles[choice - 1][0]

            # Use 'delete_from_db()' to remove the selected book from the database.
            res = delete_from_db(title_to_delete)

            # If the book is successfully deleted, print a success message.
            if res:
                print(f"Book '{title_to_delete}' deleted successfully.")
            else:
                # If the book couldn't be found (possibly due to DB issues), notify the user.
                print(f"Book '{title_to_delete}' not found.")

            # Ask the user if they want to delete another book or exit.
            continue_or_not = input(
                "Press `y` to delete another book or `exit` to exit: "
            ).lower()

            # If the user enters 'exit', exit the deletion process.
            if continue_or_not == "exit":
                return

            # If the user doesn't enter 'y' or 'exit', raise a ValueError for invalid input.
            elif continue_or_not != "y":
                raise ValueError(
                    "Invalid option. Please press `y` to continue or `exit` to exit."
                )

        # Handle invalid inputs like non-numeric values or invalid book numbers.
        except ValueError as ve:
            print(ve)  # Print the value error message.
        except Exception as e:
            # Catch any unexpected errors and print an appropriate message.
            print(f"An error occurred: {e}")
