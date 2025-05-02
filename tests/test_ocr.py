import pytest
from fastapi.testclient import TestClient
from main import app  
from io import BytesIO
from PIL import Image
import os

client = TestClient(app)  

def create_mock_image():
    img = Image.new("RGB", (100, 100), color="white")
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)
    return img_byte_arr

# Test the OCR endpoint for a single image upload 
def test_ocr_single_image():
    mock_image = create_mock_image()

    response = client.post(
        "/api/v1/ocr/",
        files={"files": ("mock_image.jpg", mock_image, "image/jpeg")}
    )

    assert response.status_code == 200

    data = response.json()
    assert "mock_image.jpg" in data
    assert isinstance(data["mock_image.jpg"], str)  

# Test OCR with multiple images upload 
def test_ocr_multiple_images():
    files = []
    for _ in range(2): 
        mock_image = create_mock_image()
        files.append(("files", ("mock_image.jpg", mock_image, "image/jpeg")))

    # Send the request to upload multiple images
    response = client.post(
        "/api/v1/ocr/",
        files=files
    )

    # Assert the response status code is 200 (successful)
    assert response.status_code == 200

    # Assert the response contains the correct structure (text extracted from images)
    data = response.json()
    for filename in data:
        assert isinstance(data[filename], str)

# Test OCR with an invalid image file type
def test_ocr_invalid_image():
    invalid_file = BytesIO(b"This is just a text file, not an image.")
    invalid_file.seek(0)

    # Send the invalid file request
    response = client.post(
        "/api/v1/ocr/",
        files={"files": ("test_invalid_file.txt", invalid_file, "text/plain")}
    )

    # Assert the response status code is 400 (Invalid file type)
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data  
    assert data["detail"] == "Invalid file type. Only jpg, jpeg, and png are allowed."


# Test OCR with an empty request (no files uploaded)
def test_ocr_no_files():
    response = client.post("/api/v1/ocr/")

    # Assert the response status code is 422 (validation error)
    assert response.status_code == 422

# Test health check endpoint
def test_healthcheck():
    response = client.get("/healthcheck")

    # Assert the response status code is 200 (live)
    assert response.status_code == 200
    assert response.json() == {"status": "live"}  

