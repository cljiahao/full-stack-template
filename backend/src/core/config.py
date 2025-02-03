from pydantic import ConfigDict, Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Base settings configuration."""

    __config__ = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


class CommonSettings(Settings):
    """Common settings for the application."""

    PROJECT_NAME: str = Field(default="My Project")
    PROJECT_VERSION: str = Field(default="v1.0.0")
    PROJECT_DESCRIPTION: str = Field(
        default="""
        This is a fancy API built with [FastAPI🚀](https://fastapi.tiangolo.com/)

        - 📝 [Source Code](https://www.github.com)
        - 🐞 [Issues](https://www.github.com/issue)
        """
    )
    ENV_STAGE: str = Field(default="stage")


class APISettings(Settings):
    """API-specific settings."""

    FASTAPI_ROOT: str = Field(default="api")
    PC_NAME: str = Field(default="localhost")
    SERVER_API_PORT: int = Field(default=8000)
    SERVER_APP_PORT: int = Field(default=5173)
    ALLOWED_CORS: list[str] = []

    def __init__(self, **data):
        super().__init__(**data)
        self.ALLOWED_CORS = self._compute_allowed_cors()

    def _compute_allowed_cors(self) -> list[str]:
        """Compute allowed CORS origins based on PC_NAME and NGINX_PORT."""
        print(self.PC_NAME)
        return [
            "http://localhost:5173",
            f"http://localhost:{self.SERVER_APP_PORT}",
            f"http://{self.PC_NAME}:{self.SERVER_APP_PORT}",
        ]

    @field_validator("FASTAPI_ROOT", mode="before")
    def remove_trailing_slash(cls, value: str) -> str:
        """Remove any trailing slashes from FASTAPI_ROOT."""
        return value.rstrip("/")


class DatabaseSettings(Settings):
    """Database configuration settings."""

    DB_NAME: str = Field(default="local.db")


class ServiceSettings(Settings):
    """Service-specific settings."""

    SERVICE_URL: str = Field(default="")


# Instantiate settings
common_settings = CommonSettings()
api_settings = APISettings()
database_settings = DatabaseSettings()
service_settings = ServiceSettings()
