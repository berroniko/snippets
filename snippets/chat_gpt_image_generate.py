from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="description of the picture",
  size="1024x1024",
  quality="standard",
  n=1,
)