from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")
    app_title: str = "App"
    allowed_origins: list[str] = [
        "127.0.0.1",
        "http://localhost:3000",
    ]
