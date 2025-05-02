
# 🚀 POS Receipt OCR & Reconciliation API

## 🧾 Overview

This project is a FastAPI-powered backend API designed to **extract and summarize POS receipt data** using OCR. It's built for use cases like fuel stations or businesses managing multiple POS machines across shifts and attendants. The API allows users to upload one or more receipts and returns the **total of successful and failed transactions**, reducing human error in shift-based reconciliation.

---

## ✅ Features

- 📸 OCR receipt parsing from images
- 📁 Support for multiple image uploads
- 📊 Transaction summary (success vs failed)
- 🧠 Pydantic-based validation and typing
- 🔄 Modular routing structure
- 🛡️ CORS support
- 🔍 Interactive API docs via Swagger UI

---

## 🗂️ Project Structure

```
pos-ocr-api/
├── api/
│   ├── db/
│   │   ├── __init__.py
│   │   └── schemas.py        # Response and request models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── ocr.py            # OCR endpoints
│   └── ocr_utils.py          # Core OCR logic
├── core/
│   ├── __init__.py
│   └── config.py             # App settings via pydantic
├── uploads/                  # Temporary image storage
├── main.py                   # FastAPI app entry point
├── requirements.txt          # Dependencies
└── README.md
```

---

## 🔧 Technologies Used

- **Python 3.12**
- **FastAPI**
- **Pydantic / Pydantic Settings**
- **Uvicorn**
- **pytesseract** (Tesseract OCR)

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pos-ocr-api.git
cd pos-ocr-api
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

- Swagger UI: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc  

---

## 📤 API Endpoints

### 🔍 OCR

- `POST /api/v1/ocr/`  
  Upload one or more receipt images to extract and summarize transaction data.

**Request (multipart/form-data):**
```bash
file: image/jpeg, image/png
```

**Response Example:**
```json
{
  "success_total": 31500,
  "failed_total": 2000,
  "receipt_count": 3,
  "breakdown": {
    "receipt_1.jpg": {
      "success": 10500,
      "failed": 0
    },
    ...
  }
}
```

---

## 📌 Future Features

- Manual correction of OCR outputs
- Receipt tagging and classification (via AI)
- Shift/attendant tracking with authentication
- Export summaries (PDF/CSV)

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🧯 Error Handling

Handles:

- Unsupported file formats
- Corrupted or unreadable images
- Empty OCR results
- Internal server errors with helpful messages

---

## 🤝 Contributing

1. Fork this repo
2. Create your branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request



## 💬 Support

Having issues or ideas? [Open an issue](https://github.com/Oguntayo/pos-ocr-api/issues) to start the conversation.