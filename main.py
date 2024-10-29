import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
openai = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = get_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chat()