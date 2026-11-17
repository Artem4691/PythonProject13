create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
"""

create_books_detail_table = """
    CREATE TABLE IF NOT EXISTS books_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
"""

add_book = 'INSERT INTO books (book_id, title, author) VALUES (?, ?, ?)'
add_book_detail = 'INSERT INTO books_detail (book_id, genre) VALUES (?, ?)'

get_books = """
SELECT b.book_id, b.title, b.author, bd.genre
FROM books b
INNER JOIN books_detail bd ON b.book_id = bd.book_id;
"""
