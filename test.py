from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "system",
            "content": "당신은 객관적으로 급식의 맛을 평가하는 인공지능입니다. 0부터 100까지의 숫자로 평가 점수를 반환하세요.",
        },
        {
            "role": "user",
            "content": str.format("다음은 오늘의 급식이야. 평가해 줘:\n{0}"),
        },
    ],
)

print(completion.choices[0].message)
