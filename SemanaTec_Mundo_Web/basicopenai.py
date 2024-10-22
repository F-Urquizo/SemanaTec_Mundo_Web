from openai import OpenAI

secret_key = ""
prompt = "Give a summary about history of Turkey"
client = OpenAI(
    api_key=secret_key,
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ],
  max_tokens = 100,
  temperature = 0
)

#print(completion)
print(completion.choices[0].message.content)
