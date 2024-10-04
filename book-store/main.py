from read_books import read_books
from insert_books import insert_books
from delete_book import delete_book


def library():
    while True:
        try:
            print("=============== Welcome to the library! ============")
            print("Press 1 to read a book")
            print("Press 2 to insert a book")
            print("Press 3 to delete a book")
            print("Enter exit to exit the library")
            print("=====================================================")

            action = input("Enter your choice: ")

            if action not in ("1", "2", "3", "exit"):
                raise ValueError("Invalid action. Please choose between 1, 2, and 3.")

            if action == "exit":
                break

            if action == "1":
                read_books()

            if action == "2":
                insert_books()

            if action == "3":
                delete_book()

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)


library()
