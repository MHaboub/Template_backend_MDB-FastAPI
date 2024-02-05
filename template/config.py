from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"


settings = Settings()