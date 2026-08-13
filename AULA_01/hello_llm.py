import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Diga olá e explique em uma frase o que é inteligência artificial."}
    ]
)

print(response.choices[0].message.content)
