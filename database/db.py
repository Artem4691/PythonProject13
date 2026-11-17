import aiosqlite
from database import queries

path_db = 'database/books.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_books_table)
        await conn.execute(queries.create_books_detail_table)
        await conn.commit()
    print('DB connected!')


async def add_book_db(book_id, title, author):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_book, (book_id, title, author))
        await conn.commit()


async def add_book_detail_db(book_id, genre):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_book_detail, (book_id, genre))
        await conn.commit()


async def get_books_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_books)
        books = await cursor.fetchall()
        return books
