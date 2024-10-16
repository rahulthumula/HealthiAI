# MultiModal AI Assistants with BillBuddy and DermatologistBot

This repository contains a collection of interactive AI-powered assistants that leverage multimodal capabilities. The assistants include **BillBuddy**, a financial assistant, and **DermatologistBot**, an expert dermatologist bot. Both utilize various AI models to perform tasks such as text extraction, expense management, and skin condition analysis.

## Features

### 1. BillBuddy: Financial Assistant
BillBuddy is designed to help users manage their bills and expenses by analyzing uploaded documents (e.g., PDFs, images). It provides insights and recommendations for effective financial management. 

- **Document Analysis:** Upload PDFs, CSVs, or text files for detailed analysis.
- **Interactive Chat Interface:** Ask questions, and get accurate responses about your expenses.
- **Automated Recommendations:** Generates follow-up questions and tips based on previous interactions.

### 2. DermatologistBot: Expert Dermatology Analysis
DermatologistBot helps users get insights on skin conditions by analyzing uploaded media (images or videos). The bot provides potential diagnoses, treatment plans, and recommendations.

- **Image and Video Analysis:** Upload media files of skin conditions for AI-based assessment.
- **Detailed Diagnoses:** Get a comprehensive analysis in JSON format with condition name, symptoms, and treatments.
- **Interactive Chat:** Ask questions about skin conditions and get responses from the bot.

## File Descriptions

### Python Scripts
- **1.py**: Contains the code for the DermatologistBot. This script initializes the bot, sets up image and PDF processing functions, and integrates with the Google Gemini API to provide dermatology-related insights. It includes methods for handling user chat and processing media files for diagnosis.

- **2.py**: Sets up utilities for embedding models and vector store usage. It includes functions for loading environment variables, initializing the Gemini multimodal model, and processing image documents. The script can be extended for more complex multi-modal processing.

- **app.py**: Runs a web-based interface for the DermatologistBot. The interface allows users to upload images or videos of skin conditions, submit text queries, and receive insights from the bot. It uses HTML and JavaScript to create a dynamic and interactive user experience.

- **multimodelgemini.py**: Implements the core logic for BillBuddy, the financial assistant. It sets up the chatbot, integrates file processing, and utilizes Google Gemini API to analyze uploaded documents for financial insights. It also includes methods for generating automated recommendations based on conversation history.

- **streamlittest.py**: A Streamlit-based application for BillBuddy. This script provides a user-friendly chat interface where users can upload files, ask questions, and get responses about their expenses. It seamlessly integrates with the core BillBuddy logic for real-time analysis and recommendations.

- **pineconeRAG.ipynb**: A Jupyter Notebook that demonstrates how to set up and use Pinecone with LangChain for Retrieval Augmented Generation (RAG). It includes code for loading PDF documents, creating vector embeddings, and using Pinecone for similarity search. The notebook serves as an example for integrating text embeddings and vector databases.

### HTML, JavaScript, and UI
- **index.html**: Provides the HTML template for the DermatologistBot's web interface. It includes sections for user input, chat display, and file uploads. The file is designed to make the chatbot experience smooth and easy to use.

- **static/mask.png, static/doctor.png, static/healthiai_logo.png**: Various static images used in the web interface for icons and logos.

- **styles.css**: Contains the CSS for styling the DermatologistBot's web interface. Ensures a clean, professional look for the chat interface.

### Configuration Files
- **.env**: Contains environment variables, including API keys for Google Gemini and Pinecone. Ensure this file is properly configured with your own credentials before running the application.

- **requirements.txt**: Lists all the Python dependencies required for the project. Use this file to set up your environment by running `pip install -r requirements.txt`.

### Miscellaneous
- **LICENSE**: The license file for the repository. This project is licensed under the MIT License.
- **README.md**: This document, providing an overview of the project, setup instructions, and detailed descriptions of each file.

## Setup

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or later
- Virtual environment (optional but recommended)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (for text extraction from images)
- [PDFPlumber](https://github.com/jsvine/pdfplumber) (for PDF extraction)
- Other dependencies listed in `requirements.txt`

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/multimodal-ai-assistants.git
   cd multimodal-ai-assistants
