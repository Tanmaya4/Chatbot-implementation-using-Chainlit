from openai import OpenAI
from src.prompt import system_instruction
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

messages = [
    {
        "role": "system",
        "content": system_instruction,
    }
]

def ask_order(messages):
    # Assuming client is an instance of the OpenAI API client or similar
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message['content']

