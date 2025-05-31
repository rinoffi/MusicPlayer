"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("28015531", None)
        self.API_HASH: str = os.environ.get("2ab4ba37fd5d9ebf1353328fc915ad28", None)
        self.SESSION: str = os.environ.get("BQGdbJEApyW1zYFxh14jXUVHCeA8o288AwFKZIj7Z2a14_WZcnIDGJCubrKP7ZgO3U6HiyE-znh878ljIj62TvLxXAg5C-XNttPNdgTzR0CVoGdDPYbC8yY-TU2PRCJ2ZmBt5zdVama4FONc0oB5EITueu5r>", None)
        self.BOT_TOKEN: str = os.environ.get("7965807385:AAFZiAyeZ4-tbWcw_bgDGwO-gx2Dr1A4x74", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("9bf74d1552e5448fa7ae9dce8ab4d909", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("792c7bb10e82450486a527acbc6f896e", None)


config = Config()
