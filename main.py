from openai import OpenAI

openai = OpenAI(
    api_key = "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"
)

def get_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [message]
    )
    return response.choices[0].message.content

 
def chat():
    while True:
        user_input = input("You ")
        if user_input == ["exit", "quit", "bye"]:
            break
        response = get_response(user_input)
        print(f"AI: , {response}")

if __name__ == "__main__":
    chat()