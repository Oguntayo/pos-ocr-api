from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse
import shutil, os
from uuid import uuid4
from api.ocr_utils import extract_text_from_image
from api.db.schemas import OCRErrorResponse
from typing import List, Dict

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post(
    "/",
    response_model=Dict[str, str],
    responses={
        500: {"model": OCRErrorResponse}
    },
    status_code=status.HTTP_200_OK,
    summary="Perform OCR on uploaded images",
    description="Upload one or more images to extract text from each."
)
async def ocr_endpoint(files: List[UploadFile] = File(...)):
    results = {}
    try:
        for file in files:
            file_ext = file.filename.split(".")[-1].lower()
            if file_ext not in ["jpg", "jpeg", "png"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid file type. Only jpg, jpeg, and png are allowed."
                )

            file_id = f"{uuid4()}.{file_ext}"
            file_path = os.path.join(UPLOAD_DIR, file_id)
            
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            text = extract_text_from_image(file_path)
            os.remove(file_path)

            results[file.filename] = text or "OCR failed or image unreadable"

        return JSONResponse(status_code=status.HTTP_200_OK, content=results)

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": str(e)}
        )
