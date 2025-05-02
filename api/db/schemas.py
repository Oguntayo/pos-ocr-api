from pydantic import BaseModel

class OCRErrorResponse(BaseModel):
    error: str
