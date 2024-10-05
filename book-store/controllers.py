import sqlite3  # Import SQLite3 module for interacting with the SQLite database.
from schema import (
    connection_to_db,
    create_table,
)  # Import utility functions for establishing connections and creating tables.


# Function to add a new book to the database.
def add_books(title, content):
    # Adds a book with a title and content to the database.
    # - title: The title of the book.
    # - content: The content of the book.
    # Returns the number of rows affected (1 if successful, 0 if not).

    try:
        conn = connection_to_db()  # Establish a connection to the SQLite database.
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries.

        create_table(conn)  # Ensure the books table exists before inserting data.

        # Insert the book's title and content into the books table using a parameterized query.
        cursor.execute(
            """
            INSERT INTO books (title, content) VALUES (?, ?)
            """,
            (title, content),
        )
        conn.commit()  # Commit the transaction to save the changes to the database.

        return (
            cursor.rowcount
        )  # Return the number of rows affected (should be 1 if the book was added successfully).

    except sqlite3.IntegrityError:
        # Handle the case where the book already exists (integrity constraint violation).
        print(f"Error: The book '{title}' already exists in the database.")
        conn.rollback()  # Rollback the transaction to undo the changes.
        return 0  # Return 0 to indicate failure.

    except sqlite3.OperationalError as oe:
        # Handle database operational errors (e.g., issues with the database schema).
        print(f"Operational error occurred while adding the book: {oe}")
        conn.rollback()  # Rollback the transaction in case of error.
        return 0

    except sqlite3.Error as e:
        # Handle generic SQLite errors that might occur during the process.
        print(f"SQLite error occurred while adding the book: {e}")
        conn.rollback()  # Rollback the transaction.
        return 0

    except Exception as e:
        # Catch-all for any unexpected errors.
        print(f"An unexpected error occurred while adding the book: {e}")
        return 0

    finally:
        # Ensure that the database connection is closed, whether or not the operation succeeded.
        if conn:
            conn.close()


# Function to fetch all book titles from the database.
def get_titles():
    # Retrieves the list of all book titles from the database.
    # Returns a list of book titles or an empty list if there are errors.

    try:
        conn = connection_to_db()  # Establish a connection to the database.
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries.

        # Execute the SQL query to select all book titles from the 'books' table.
        cursor.execute("SELECT title FROM books")
        titles = (
            cursor.fetchall()
        )  # Fetch all results (titles) from the executed query.

        return titles  # Return the list of titles.

    except sqlite3.OperationalError as oe:
        # Handle any operational errors during the database operation.
        print(f"An Operational Error occurred while fetching titles: {oe}")
        return []

    except sqlite3.Error as e:
        # Handle generic SQLite errors.
        print(f"An SQLite Error occurred while fetching titles: {e}")
        return []

    except Exception as e:
        # Handle unexpected errors.
        print(f"An unexpected error occurred while fetching titles: {e}")
        return []

    finally:
        # Ensure the database connection is closed.
        if conn:
            conn.close()


# Function to retrieve the content of a book in "pages" (limited number of characters per page).
def get_books(title):
    # Retrieves the content of a book, split into pages (100 characters per page).
    # - title: The title of the book to fetch.
    # Returns a list of pages, where each page is a string containing up to 100 characters.

    try:
        conn = connection_to_db()  # Establish a connection to the database.
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries.

        # Execute the SQL query to fetch the content of the book where the title matches.
        cursor.execute("SELECT content FROM books WHERE title = ?", (title,))

        book = cursor.fetchone()  # Fetch the first (and only) result.

        if book is None:
            # If no book is found with the given title, return an empty list.
            return []

        content = book[0]  # Extract the book's content from the result.
        max_chars = 100  # Define the maximum number of characters per page.
        # Split the content into pages, with each page containing up to 'max_chars' characters.
        pages = [content[i : i + max_chars] for i in range(0, len(content), max_chars)]

        return pages  # Return the list of pages (content split into chunks).

    except sqlite3.OperationalError as oe:
        # Handle operational errors that occur during the fetch operation.
        print(f"An Operational Error occurred while fetching book content: {oe}")
        return []

    except sqlite3.Error as e:
        # Handle generic SQLite errors.
        print(f"An SQLite Error occurred while fetching book content: {e}")
        return []

    except Exception as e:
        # Handle unexpected errors.
        print(f"An unexpected error occurred while fetching book content: {e}")
        return []

    finally:
        # Ensure the connection to the database is closed.
        if conn:
            conn.close()


# Function to delete a book from the database.
def delete_book(title):
    # Deletes a book from the database by its title.
    # - title: The title of the book to delete.
    # Returns the number of rows affected (1 if successful, 0 if no book was deleted).

    try:
        conn = connection_to_db()  # Establish a connection to the database.
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries.

        # Execute the SQL query to delete the book where the title matches.
        cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        conn.commit()  # Commit the transaction to confirm the deletion.

        return cursor.rowcount  # Return the number of rows affected (1 if successful).

    except sqlite3.IntegrityError as ie:
        # Handle integrity errors that might occur during the deletion.
        print(f"Integrity error occurred while deleting the book: {ie}")
        conn.rollback()  # Rollback the transaction in case of error.
        return 0

    except sqlite3.OperationalError as oe:
        # Handle operational errors (e.g., issues with the database).
        print(f"Operational error occurred while deleting the book: {oe}")
        conn.rollback()  # Rollback the transaction.
        return 0

    except Exception as e:
        # Catch-all for any unexpected errors.
        print(f"An unexpected error occurred while deleting the book: {e}")
        conn.rollback()  # Rollback the transaction.
        return 0

    finally:
        # Ensure the connection to the database is closed.
        if conn:
            conn.close()
