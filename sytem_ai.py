from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-40",
  messages=[
    {
      "role":"system",
      "content":"You will be provided with a price of code, and your task is to explain it in a concise way."
    },
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
