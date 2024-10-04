import google.generativeai as genai
import time
import json
import os
import logging
from dotenv import load_dotenv
from google.api_core import retry
from api_key import api_key

genai.configure(api_key=api_key)

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a retry strategy to handle potential API call failures
billbuddy_retry = retry.Retry(
    initial=2.0,  # Initial retry delay in seconds
    maximum=10.0,  # Maximum retry delay in seconds
    multiplier=1.0,  # Multiplier for exponential backoff
    deadline=60.0  # Overall deadline for retries in seconds
)

class BillBuddy:
    def __init__(self):
        self.system_instruction = "You are an expert financial assistant specializing in managing bills and expenses."
        self.model = genai.GenerativeModel("models/gemini-1.5-pro-latest", system_instruction=self.system_instruction)

        recommendation_system_prompt = """
        You are a financial assistant helping a user manage their bills. You should:
        - Review the conversation history.
        - Generate a follow-up question or a new topic (such as budgeting, payment options, or disputes).
        - The question should be concise and no more than 15 words.
        Return the question.
        """
        self.recommendation_model = genai.GenerativeModel("models/gemini-1.5-flash", system_instruction=recommendation_system_prompt)
        self.messages = []

    @billbuddy_retry
    def generate_response(self, prompt) -> str:
        try:
            self.messages.append({'role': 'user', 'parts': [prompt]})
            response = self.model.generate_content(self.messages)
            self.messages.append({'role': 'assistant', 'parts': [response.candidates[0].content]})
            return response.candidates[0].content
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "Sorry, something went wrong while processing your request."

    @billbuddy_retry
    def process_file(self, file_path) -> dict:
        try:
            file = genai.upload_file(path=file_path)
            while file.state.name == "PROCESSING":
                time.sleep(1)
                file = genai.get_file(file.name)
            if file.state.name == "FAILED":
                raise ValueError(f"File processing failed: {file.state.name}")

            prompt = f"""
            Analyze the uploaded file in detail and provide a comprehensive summary of the user's expenses...
            File: {file}
            Detailed Analysis: 
            """
            self.messages.append({'role': 'user', 'parts': [prompt]})
            response = self.model.generate_content(
                self.messages, 
                generation_config={"response_mime_type": "application/json"},
                request_options={"timeout": 120}
            )

            response_content = response.candidates[0].content
            if isinstance(response_content, str):
                return json.loads(response_content)
            else:
                logger.error(f"Expected a JSON string but got {type(response_content).__name__}: {response_content}")
                return {"error": "Expected JSON response, got something else. Please check the logs."}
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            return {"error": "File processing failed."}

    @billbuddy_retry
    def recommend_question(self) -> str:
        try:
            formatted_messages = [{"role": message["role"], "text": message["content"]} for message in self.messages]
            prompt = f"Read the conversation history and provide a question.\nConversation history: {formatted_messages}"
            response = self.recommendation_model.generate_content([{'role': 'user', 'text': prompt}])
            return response.candidates[0].content.strip()
        except Exception as e:
            logger.error(f"Error generating recommendation: {e}")
            return "Sorry, something went wrong while generating a recommendation."

if __name__ == "__main__":
    bill_buddy = BillBuddy()
    file_path = "temp_image.jpg"  # Replace with the actual path to your PDF file
    analysis_results = bill_buddy.process_file(file_path)
    print(f"Analysis Results: {analysis_results}")
