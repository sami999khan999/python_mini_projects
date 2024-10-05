import sqlite3  # Import the sqlite3 module to work with SQLite databases.


# This function establishes a connection to the SQLite database.
# If the database doesn't exist, SQLite will automatically create it.
# The default database name is "books.db", but you can pass a different name as an argument.
def connection_to_db(db_name="books.db"):
    return sqlite3.connect(
        db_name
    )  # Returns a connection object to interact with the database.


# This function creates a table in the specified database connection.
# By default, it creates a table named "books" unless another table name is provided.
def create_table(conn, table_name="books"):
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands.

    # Execute an SQL command to create the "books" table if it doesn't already exist.
    # The table will have three columns:
    # 1. 'id' (Primary Key, auto-incrementing integer).
    # 2. 'title' (Unique text, representing the title of the book).
    # 3. 'content' (Text, representing the book's content).
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL
        )
        """
    )

    conn.commit()  # Commit the transaction to the database to save changes.
