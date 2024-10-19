from environs import Env

class Config:
    def __init__(self):
        self.env = Env()
        self.env.read_env()

        self.api_id: int = self.env.int("API_ID")
        self.api_hash: str = self.env.str("API_HASH")
        self.token: str = self.env.str("TOKEN")

config = Config()
