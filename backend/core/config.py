import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

from secrets import token_bytes
from base64 import b64encode


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    # if empty -generate one in bash: $ openssl rand -hex 32
    if not SECRET_KEY:
        #Generate a new SECRET_KEY example : '75b6639905a352248601f7c2d1539cb3de3bc038f25cc2acf5213fcd0e91465c'
        SECRET_KEY = b64encode(token_bytes(32)).decode()
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()
