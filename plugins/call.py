from pyrogram import types, Client, filters, errors

from utils.logger import logger
from utils.funcs import full_name, emoji_list

import asyncio, random


@Client.on_message(filters.command(["all"], prefixes=[".", "/", "!"]) & filters.group)
async def tag_cmd(_, msg: types.Message):
    try:
        
        members = list()
        async for member in _.get_chat_members(msg.chat.id):
            members.append(member)

        users = [member for member in members if member.user and not member.user.is_bot and not member.user.is_deleted]
        print(users)

        mentioned_users = (f"<b>{full_name(msg)}</b> called everyone"
                           f"\n{f'<i>{msg.text.split(maxsplit=1)[1]}</i>' if len(msg.text.split()) > 1 else ''}\n\n")
        i = 0

        for user in users:
            mentioned_users += f"<a href='tg://user?id={user.user.id}'>{random.choice(await emoji_list())}</a> "
            i += 1
            if i == 10:
                try:
                    await _.send_message(
                        chat_id=msg.chat.id,
                        text=mentioned_users
                    )
                except errors.FloodWait:
                    await asyncio.sleep(1)

                    await _.send_message(
                        chat_id=msg.chat.id,
                        text=mentioned_users
                    )

                i = 0
                mentioned_users = ""

        if mentioned_users:
            await _.send_message(chat_id=msg.chat.id, text=mentioned_users)

    except Exception as e:
        logger.error(e)

