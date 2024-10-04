import sqlite3
from schema import connection_to_db, create_table


def add_books(title, content):
    try:
        conn = connection_to_db()
        cursor = conn.cursor()

        create_table(conn)

        cursor.execute(
            """
            INSERT INTO books (title, content) VALUES (?, ?)
            """,
            (title, content),
        )
        conn.commit()

        return cursor.rowcount

    except sqlite3.IntegrityError:
        print(f"Error: The book '{title}' already exists in the database.")
        conn.rollback()  # Roll back in case of integrity issues
        return 0

    except sqlite3.OperationalError as oe:
        print(f"Operational error occurred: {oe}")
        conn.rollback()  # Roll back on operational errors
        return 0

    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
        conn.rollback()
        return 0

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

    finally:
        if conn:
            conn.close()  # Ensure connection is closed


def get_titles():
    try:
        conn = connection_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM books")
        titles = cursor.fetchall()

        return titles

    except Exception as e:
        print(f"An error occurred while fetching titles: {e}")
        return []

    finally:
        if conn:
            conn.close()


def get_books(title):
    try:
        conn = connection_to_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT content FROM books WHERE title = ?",
            (title,),
        )

        book = cursor.fetchone()

        if book is None:
            print(f"No book found with the title: {title}")
            return []  # Return an empty list if no book is found

        content = book[0]
        max_chars = 100
        pages = [content[i : i + max_chars] for i in range(0, len(content), max_chars)]

        return pages

    except Exception as e:
        print(f"An error occurred while fetching the book content: {e}")
        return []

    finally:
        if conn:
            conn.close()


def delete_book(title):
    try:
        conn = connection_to_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        conn.commit()  # Commit the delete operation

        return cursor.rowcount

    except sqlite3.IntegrityError as ie:
        print(f"Integrity error occurred while deleting: {ie}")
        conn.rollback()  # Roll back in case of integrity issues

    except sqlite3.OperationalError as oe:
        print(f"Operational error occurred while deleting: {oe}")
        conn.rollback()  # Roll back on operational errors

    except ValueError as ve:
        print(ve)  # Handle value errors separately for clarity

    except Exception as e:
        print(f"An unexpected error occurred while deleting: {e}")
        conn.rollback()  # Roll back on unexpected errors

    finally:
        if conn:
            conn.close()  # Ensure connection is closed
