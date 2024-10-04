from controllers import get_titles, get_books, add_books


def insert_books():
    try:
        while True:
            title = input("Enter the title of the book: ")
            content = input("Enter the content of the book: ")

            res = add_books(title, content)

            if res:
                print(f"Book '{title}' added successfully!")
            else:
                print(f"Cannot add book '{title}'!")

            choice = input(
                "Press `y` if you would like to add another book or press `exit` to exit: "
            ).lower()

            if choice == "y":
                continue
            elif choice == "exit":
                break
            else:
                raise ValueError("Enter a valid option.")

    except ValueError as ve:
        print(ve)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
