from controllers import (
    get_titles,
    get_books,
)  # Import functions to fetch book titles and content.


# Define the 'read_books' function which allows the user to read books from the database.
def read_books():

    # Start a while loop that allows the user to select a book and navigate its pages.
    while True:
        try:
            # Fetch the list of available book titles.
            titles = get_titles()

            # If no titles are available, notify the user and exit the function.
            if not titles:
                print("There are no books available!")
                return  # Exit the function if no books are found.

            # Display the available book titles to the user.
            print("Here are the books available")
            for idx, (title,) in enumerate(
                titles
            ):  # Enumerate over the list of titles.
                print(
                    f"{idx + 1}: {title}"
                )  # Display the book title with a corresponding number.

            # Ask the user to choose a book by entering its corresponding number.
            user_input = input("Enter the number corresponding to the book: ")

            # Allow the user to exit the book selection process.
            if user_input == "exit":
                break  # Exit the while loop if 'exit' is entered.

            # Convert the user input to an integer to match the book's index.
            choice = int(user_input)

            # Ensure the user's choice is valid, i.e., within the range of available titles.
            if choice < 1 or choice > len(titles):
                print("Please choose a number corresponding to the book.")
                continue  # Return to the top of the loop to ask for valid input.

            # Retrieve the selected book's title and its corresponding pages.
            title = titles[choice - 1][0]  # Get the title using the user's choice.
            pages = get_books(title)  # Fetch the book's content by calling 'get_books'.

            # If no content is found for the selected book, notify the user and continue.
            if not pages:
                print("No content found for this book.")
                continue

            # Initialize 'page_number' to track the current page.
            page_number = 0

            # Display the first page of the selected book.
            print(f"Title: {title}")
            print(f"Content: {pages[page_number]}")  # Display the first page's content.
            print(
                f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
            )  # Display page number and total pages.

            # Start another loop to allow the user to navigate through pages.
            while True:
                # Prompt the user to navigate to the previous or next page, or exit.
                page_action = input(
                    "Enter `p` for previous page, `n` for next page and `exit` to exit: "
                ).lower()

                # Ensure the user input is valid.
                if page_action not in ("p", "n", "exit"):
                    print("Enter a valid input.")
                    continue  # Continue the loop to ask for valid input.

                # Break out of the loop if the user wants to exit page navigation.
                if page_action == "exit":
                    break

                # Handle the user's request to go to the previous page.
                if page_action == "p":
                    # If the user is already on the first page, notify them.
                    if page_number == 0:
                        print("This is the First page")
                    else:
                        # Otherwise, move to the previous page and display its content.
                        page_number -= 1
                        print(f"Content: {pages[page_number]}")
                        print(
                            f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
                        )

                # Handle the user's request to go to the next page.
                elif page_action == "n":
                    # If the user is already on the last page, notify them.
                    if page_number == len(pages) - 1:
                        print("This is the Last page")
                    else:
                        # Otherwise, move to the next page and display its content.
                        page_number += 1
                        print(f"Content: {pages[page_number]}")
                        print(
                            f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
                        )

        # Handle errors related to invalid input (e.g., when user input is not an integer).
        except ValueError:
            print("Please enter a valid number.")

        # Handle any other exceptions that may occur during the process.
        except Exception as e:
            print(f"An error occurred: {e}")
