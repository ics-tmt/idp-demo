from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Application settings and environment variables for JIRA connectivity.
    """
    JIRA_URL: str
    JIRA_USERNAME: str
    JIRA_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
