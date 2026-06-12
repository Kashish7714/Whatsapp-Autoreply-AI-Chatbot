import os
import pyperclip
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your_api_key_here"))


command = pyperclip.paste()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a person name harry who speaks in hindi as well english. He is from india and is a coder. You analyze chat history and respond (text message only)"
        },
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)  
