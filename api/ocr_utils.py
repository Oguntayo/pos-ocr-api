import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from core.config import settings 
from typing import List, Optional 

def preprocess_image(image_path: str) -> Optional[Image.Image]:
    try:
        img = Image.open(image_path)
        img = img.convert('L')
        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = img.filter(ImageFilter.SHARPEN)
        threshold = 128
        img = img.point(lambda x: 0 if x < threshold else 255, '1')
        return img
    except Exception as e:
        return None

def extract_text_from_image(
    image_path: str,
    tesseract_path: Optional[str] = None,
    lang: str = None, 
    psm: int = None, 
    oem: int = None  
) -> Optional[str]:
    try:
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
        lang = lang or settings.OCR_LANG
        psm = psm or settings.OCR_PSM
        oem = oem or settings.OCR_OEM
        
        img = preprocess_image(image_path)
        if img is None:
            return None
        config = f'--psm {psm} --oem {oem}'
        return pytesseract.image_to_string(img, lang=lang, config=config).strip()
    except Exception as e:
        return None

def extract_text_from_images(
    image_paths: List[str],
    tesseract_path: Optional[str] = None,
    lang: str = None,
    psm: int = None,
    oem: int = None
) -> List[Optional[str]]:
    return [extract_text_from_image(p, tesseract_path, lang, psm, oem) for p in image_paths]
