from pyrogram import types

import requests


def full_name(msg: types.Message) -> str:
    return f"{msg.from_user.first_name}{' ' + msg.from_user.last_name if msg.from_user.last_name else ''}"

async def emoji_list() -> str:
    url = "https://raw.githubusercontent.com/leodr/generate-emoji-list/main/lists/emojis-en-v14.0.json"
    req = requests.get(url).json()

    e = []
    for category in req:
        for emoji in category['emojis']:
            e.append(emoji[0])

    return ''.join(e)
