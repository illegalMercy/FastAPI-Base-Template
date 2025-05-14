from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseModel):
    url: PostgresDsn
    echo: bool = True

    name_convention: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class UvicornConfig(BaseModel):
    host: str
    port: int


class Settings(BaseSettings):
    debug: bool
    uvicorn: UvicornConfig
    postgres: PostgresConfig
    model_config = SettingsConfigDict(
        env_file=(".env.example", ".env"),
        env_prefix="APP__",
        case_sensitive=False,
        env_nested_delimiter="__",
    )


settings = Settings()
