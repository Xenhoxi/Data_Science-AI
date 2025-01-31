from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("API_KEY"),
)
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about antoine"}
    ]
)

with open('message_antoine.txt', 'w') as file:
    file.write(str(completion))
    file.write("\n")
    file.write(str(completion.choices[0].message.content))
