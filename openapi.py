from openai import OpenAI

client = OpenAI(OPENAI_API_KEY)

response = client.images.generate(
  model = "dall-e-3",
  prompt = "Brad Pitt at a Golf Course.",
  size = "1792x1024",
  quality="standard",
  n=1
)

image_url = response.data[0].url

print(image_url)
