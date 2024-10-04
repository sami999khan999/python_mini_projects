import sqlite3


def connection_to_db(db_name="books.db"):
    return sqlite3.connect(db_name)


def create_table(conn, table_name="books"):
    cursor = conn.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL
        )
        """
    )

    conn.commit()
