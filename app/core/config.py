from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Приложение для бронирование переговорок'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
