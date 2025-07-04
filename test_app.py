
import pytest
from fastapi.testclient import TestClient
from fast_api import app  # Assuming your FastAPI app is in 'backend.py'
from unittest.mock import patch, MagicMock
from io import BytesIO

# Create a client to interact with the application in tests
client = TestClient(app)

@pytest.fixture
def mock_llm():
    """Fixture to mock the GoogleLLM class."""
    with patch('backend.GoogleLLM') as mock:
        # Configure the mock to simulate the behavior of the real LLM
        mock_instance = MagicMock()
        mock_instance.generate.return_value = "This is a mock review."
        mock.return_value = mock_instance
        yield mock

def create_dummy_pdf():
    """Creates a dummy PDF file in memory for testing."""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "This is a test resume.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def test_resume_review_success(mock_llm):
    """Test the /resume-review endpoint for a successful PDF upload."""
    dummy_pdf = create_dummy_pdf()
    
    # Simulate a file upload
    files = {'file': ('test_resume.pdf', dummy_pdf, 'application/pdf')}
    data = {'api_key': 'test_api_key'}

    # Make the request to the test client
    response = client.post("/resume-review", files=files, data=data)

    # Assert that the request was successful
    assert response.status_code == 200
    
    # Assert that the response contains the expected content
    response_json = response.json()
    assert response_json["message"] == "Review generated successfully"
    assert response_json["content"] == "This is a mock review."

def test_unsupported_file_type():
    """Test the endpoint with a non-PDF file to ensure it's rejected."""
    # Simulate uploading a plain text file instead of a PDF
    files = {'file': ('test.txt', b'this is not a pdf', 'text/plain')}
    data = {'api_key': 'test_api_key'}

    response = client.post("/resume-review", files=files, data=data)

    # Assert that the server responds with a 400 Bad Request error
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

