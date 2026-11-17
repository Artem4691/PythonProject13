from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_commands = Router()


@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}!\n'
        f'Это бот-каталог книг.\n'
        f'Команды:\n'
        f'/add_book - добавить книгу\n'
        f'/books - список книг'
    )
