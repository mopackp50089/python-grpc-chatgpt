import openai
import os

# load from .env
from dotenv import load_dotenv
load_dotenv()

def gptTurbo(role, content):
  # set env variable -> export OPENAI_API_KEY=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
  openai.api_key = os.getenv("OPENAI_API_KEY")
  resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        # {"role": "system", "content": "You are a helpful and funny assistant,你很會說故事,你只能用繁體中文回答我"},
        {"role": role, "content": content},
        ]
  )
  print(resp['choices'][0]['message']['content'])
  return resp['choices'][0]['message']['content']

# GPT3
# resp = openai.Completion.create(model="text-davinci-003", prompt="吃蘋果的好處", temperature=0, max_tokens=500)
# print(resp["choices"][0]["text"])


