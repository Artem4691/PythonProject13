import logging
import asyncio
from aiogram.types import BotCommand
from config import bot, dp
from heandlers import commands, fsm
from database import db


async def set_commands():
    bot_commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='add_book', description='Добавить книгу'),
        BotCommand(command='books', description='Список книг')
    ]
    await bot.set_my_commands(bot_commands)


async def on_startup():
    await db.init_db()
    await set_commands()
    print('Бот включен!')


dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm.router_fsm)

dp.startup.register(on_startup)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))

