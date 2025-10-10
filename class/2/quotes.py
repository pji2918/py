import os.path
import random

if not os.path.isfile("excludedQuotes.txt"):
    open("excludedQuotes.txt", mode="w")

with open("excludedQuotes.txt", mode="r+", encoding="utf-8") as f:
    quotes = [
        "시작이 반이고 가만히 있으면 반은 가니까, 시작하고 가만히 있으면 끝이다.",
        "어떤 사람에게는 1초가 1시간이 될 수 있다.",
        "오늘 아침 뭐 먹지",
        "오늘 점심 뭐 먹지",
        "오늘 저녁 뭐 먹지",
    ]

    for i in f.readlines():
        if i.strip() in quotes:
            quotes.remove(i.strip())

    # weekday = ["월", "화", "수", "목", "금"]

    print("#" * 15)
    # print(f"# {weekday[i]}요일의 명언 #")
    print("# 오늘의 명언 #")
    print("#" * 15)
    print()

    if len(quotes) <= 0:
        print("더 이상 명언이 없습니다.")
        print()
    else:
        todaysQuote = random.choice(quotes)
        print(todaysQuote)
        # quotes.remove(todaysQuote)
        f.write(todaysQuote + "\n")
        print()
