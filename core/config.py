import secrets
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "POS OCR API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = (
        "A backend API for managing POS receipt reconciliation across shifts, attendants, and pumps "
        "using OCR to extract transaction summaries from printed receipts."
    )

    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = True  
    TESTING: bool = False

    UPLOAD_DIR: str = "uploads"
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png"]

    OCR_LANG: str = "eng"
    OCR_PSM: int = 3
    OCR_OEM: int = 3

    class Config:
        env_file = ".env"

settings = Settings()
