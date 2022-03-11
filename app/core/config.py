from pydantic import BaseSettings, Field, validator

class Settings(BaseSettings):
    CLIENT_DISCORD_TOKEN: str = Field(..., env='CLIENT_DISCORD_TOKEN')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()