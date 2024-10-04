import pytesseract
from PIL import Image
import pdfplumber

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        if extracted_text.strip():
            print(f"Text successfully extracted from image: {image_path}")
            print(extracted_text)
        else:
            print(f"No text extracted from image: {image_path}")
    except Exception as e:
        print(f"Failed to extract text from image: {image_path}. Error: {str(e)}")

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text
        if extracted_text.strip():
            print(f"Text successfully extracted from PDF: {pdf_path}")
            print(extracted_text)
        else:
            print(f"No text extracted from PDF: {pdf_path}")
    except Exception as e:
        print(f"Failed to extract text from PDF: {pdf_path}. Error: {str(e)}")

# Paths to the files
image_file_path = 'C:/Users/rahul/OneDrive/Desktop/expense_tracker/temp_image.jpg'
pdf_file_path = 'C:/Users/rahul/OneDrive/Desktop/expense_tracker/G046706069.pdf'

# Extract text
extract_text_from_image(image_file_path)
extract_text_from_pdf(pdf_file_path)