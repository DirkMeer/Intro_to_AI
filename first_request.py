import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


duck_instructions = """
You are a duck. You will answer the question in a helpful manner but do not forget to quack every few words.

My question is: What is the fastest animal on Earth?
"""

print("Asking DuckGPT...")
duck_response = CLIENT.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": duck_instructions}
    ]
)

quack_talk = duck_response.choices[0].message.content

print(f"The duck says: {quack_talk}")