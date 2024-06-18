from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_env: str
    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_pool_timeout: int = 30
    db_pool_recycle: int = 1800
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str

    model_config = SettingsConfigDict(env_file='.env')

    @property
    def postgres_url(self):
        return f'postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'


settings = Settings()
