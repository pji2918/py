from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful programming assistant."},
        {
            "role": "user",
            "content": "Python에서 random.randint를 사용할 때 /dev/urandom과 같은 시스템 엔트로피를 사용하지 않으려면 어떻게 해야 하나요?",
        },
    ],
)

print(completion.choices[0].message)
