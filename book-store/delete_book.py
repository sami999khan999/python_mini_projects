from controllers import get_titles, delete_book as delete_from_db


def delete_book():
    while True:
        try:
            titles = get_titles()

            if not titles:
                print("No books available to delete.")
                return

            for idx, (title,) in enumerate(titles):
                print(f"{idx + 1}: {title}")

            user_input = input(
                "Enter a number corresponding to the book you want to delete or 'exit' to exit: "
            )

            if user_input.lower() == "exit":
                return

            choice = int(user_input)

            if choice < 1 or choice > len(titles):
                raise ValueError("Invalid choice!")

            title_to_delete = titles[choice - 1][0]
            res = delete_from_db(title_to_delete)

            if res:
                print(f"Book '{title_to_delete}' deleted successfully.")
            else:
                print(f"Book '{title_to_delete}' not found.")

            continue_or_not = input(
                "Press `y` to delete another book or `exit` to exit: "
            ).lower()

            if continue_or_not == "exit":
                return
            elif continue_or_not != "y":
                raise ValueError(
                    "Invalid option. Please press `y` to continue or `exit` to exit."
                )

        except ValueError as ve:
            print(ve)  # Print the value error message
        except Exception as e:
            print(f"An error occurred: {e}")  # General error handling
