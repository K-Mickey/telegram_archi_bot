import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram_sqlite_storage.sqlitestore import SQLStorage

from bin.handler import main_commands, feedback, suggestion, question
from bin.handler.admin import admin
from bin.ect import cfg


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
bot = Bot(cfg.BOT_TOKEN, parse_mode=ParseMode.HTML)


async def run() -> None:
    storage = SQLStorage(cfg.PATH_STORAGE)
    dp = Dispatcher(storage=storage)
    dp.include_routers(
        main_commands.router,
        feedback.router,
        suggestion.router,
        question.router,
        admin.router,
    )

    await dp.start_polling(bot)
