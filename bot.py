from pyrogram import Client, enums

from misc.config import config


class PyroClient:
    def __init__(
            self,
            api_id: int | None = config.api_id,
            api_hash: str | None = config.api_hash,
            token: str | None = config.token,
            parse_mode: enums.ParseMode | None = enums.ParseMode.HTML
    ):
        self.client = Client(
            "SESSION",
            bot_token=token,
            api_id=api_id,
            api_hash=api_hash,
            parse_mode=parse_mode,
            plugins=dict(root="plugins")
        )

    async def start(self):
        await self.client.start()

    def run(self):
        self.client.run()

client = PyroClient()
