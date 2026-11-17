from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from database.db import add_book_db, add_book_detail_db, get_books_db

router_fsm = Router()


class BookForm(StatesGroup):
    book_id = State()
    title = State()
    author = State()
    genre = State()


@router_fsm.message(Command('add_book'))
async def start_add_book(message: Message, state: FSMContext):
    await state.set_state(BookForm.book_id)
    await message.answer('Введите номер книги:')


@router_fsm.message(BookForm.book_id)
async def add_book_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Ошибка! Номер книги должен быть числом. Попробуйте еще раз:')
        return

    await state.update_data(book_id=int(message.text))
    await state.set_state(BookForm.title)
    await message.answer('Введите название книги:')


@router_fsm.message(BookForm.title)
async def add_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(BookForm.author)
    await message.answer('Введите автора книги:')


@router_fsm.message(BookForm.author)
async def add_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(BookForm.genre)
    await message.answer('Введите жанр книги:')


@router_fsm.message(BookForm.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()

    await add_book_db(
        book_id=data['book_id'],
        title=data['title'],
        author=data['author']
    )
    await add_book_detail_db(
        book_id=data['book_id'],
        genre=data['genre']
    )

    await message.answer(
        f"Книга добавлена!\n"
        f"Номер: {data['book_id']}\n"
        f"Название: {data['title']}\n"
        f"Автор: {data['author']}\n"
        f"Жанр: {data['genre']}"
    )
    await state.clear()


@router_fsm.message(Command('books'))
async def get_books(message: Message):
    books = await get_books_db()

    if not books:
        await message.answer('В каталоге пока нет книг!')
        return

    for book_id, title, author, genre in books:
        await message.answer(
            f"Номер: {book_id}\n"
            f"Название: {title}\n"
            f"Автор: {author}\n"
            f"Жанр: {genre}"
        )
