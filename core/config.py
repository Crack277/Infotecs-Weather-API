from pathlib import Path

__BASE__ = Path(__file__).parent.parent


class Settings:
    db_url: str = f"sqlite+aiosqlite:///{__BASE__}/database.db"
    db_echo: bool = True

settings = Settings()