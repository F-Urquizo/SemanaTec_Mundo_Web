from openai import OpenAI

#secret_key = "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"
secret_key = "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"
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
