from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "너는 알아도 전혀 쓸모없는 사실을 알려주는 챗봇이야.",
        },
        {"role": "user", "content": "알아도 전혀 쓸모없는 사실을 한 문장으로 알려줘."},
    ],
    max_tokens=100,
)

print(completion.choices[0].message.content)
