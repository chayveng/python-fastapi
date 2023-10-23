from pydantic import BaseSetting

POSTGRES_DATABASE_URL = "postgresql://postgres:h48EzLgaSmO6FXpS@localhost/example"

class Config(BaseSetting):
    PROJECT_NAME = "FAST API"

