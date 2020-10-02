import sqlite3


def connect():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER  PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()
connect()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()  # cursor.fetchall() fetches all the rows of a query result. It returns all the rows as a
    # list of tuples. An empty list is returned if there is no record to fetch.
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=? ", (title, author, year, isbn))
    rows = cur.fetchall()  # cursor.fetchall() fetches all the rows of a query result. It returns all the rows as a
    # list of tuples. An empty list is returned if there is no record to fetch.
    conn.close()
    return rows


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

