from controllers import get_titles, create_table, get_books


def read_books():

    while True:
        try:
            titles = get_titles()

            if not titles:
                print("There are no books available!")
                return

            print("Here are the books available")
            for idx, (title,) in enumerate(titles):
                print(f"{idx + 1}: {title}")

            user_input = input("Enter the number corresponding to the book: ")

            if user_input == "exit":
                break

            choice = int(user_input)

            if choice < 1 or choice > len(titles):
                print("Please choose a number corresponding to the book.")
                continue

            title = titles[choice - 1][0]
            pages = get_books(title)

            if not pages:
                print("No content found for this book.")
                continue

            page_number = 0

            print(f"Title: {title}")
            print(f"Content: {pages[page_number]}")
            print(
                f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
            )

            while True:
                page_action = input(
                    "Enter `p` for previous page, `n` for next page and `exit` to exit: "
                ).lower()

                if page_action not in ("p", "n", "exit"):
                    print("Enter a valid input.")
                    continue

                if page_action == "exit":
                    break

                if page_action == "p":
                    if page_number == 0:
                        print("This is the First page")
                    else:
                        page_number -= 1
                        print(f"Content: {pages[page_number]}")
                        print(
                            f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
                        )

                elif page_action == "n":
                    if page_number == len(pages) - 1:
                        print("This is the Last page")
                    else:
                        page_number += 1
                        print(f"Content: {pages[page_number]}")
                        print(
                            f"--------------------------{page_number + 1} of {len(pages)}------------------------------"
                        )

        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
