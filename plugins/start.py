from pyrogram import types, Client, filters

from utils.logger import logger
from utils.funcs import full_name
from misc import text


@Client.on_message(filters.command(['start'], prefixes=['!', '.', '/']))
async def start_handler(_, msg: types.Message):
    try:
        await msg.reply(text.START_MESSAGE.format(name=full_name(msg)))

    except Exception as e:
        logger.error(e)
