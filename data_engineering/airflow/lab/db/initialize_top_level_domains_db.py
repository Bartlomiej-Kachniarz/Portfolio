import os
import sqlite3
from sqlite3 import Error

path_to_db = os.getcwd()


def create_conn(db_file):
    """Create a connection to the SQLite database.

    Args:
        db_file (db): database file to connect to

    Returns:
        Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print("Error connecting to SQLite database: {e}")
        return None


def create_table(conn, create_table_sql_query):
    """Create a table in the SQLite database using given SQL query.

    Args:
        conn (conn): Connection object
        create_table_sql_query (sql): SQL query file
    """
    try:
        cc = conn.cursor()
        cc.execute(create_table_sql_query)
    except Error:
        print("Error while creating table. {e}")


def create_table_in_db():
    db_path = rf"{path_to_db}/manual_top_level_domains_db.db"

    conn = create_conn(db_path)

    if conn is not None:
        with open(f"{path_to_db}/sql/create_manual_load_table.sql", "r") as f:
            sql_query = f.read()
            create_table(conn, sql_query)
    else:
        print(f"Something went wrong! Database path {path_to_db}")


if __name__ == "__main__":
    create_table_in_db()
