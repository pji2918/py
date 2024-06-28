from io import StringIO
import pandas as pd
import requests as rq
import datetime
import os
import openai

ai = openai.OpenAI(api_key="sk-proj-bFNw2Oan264wwmkfQwn0T3BlbkFJHkzw1T7RBULqu6wK2j0w")


dateipt = input("날짜를 입력하세요(YYYYMMDD 형식으로 날짜 입력 혹은 TODAY, NOW) : ")

try:
    if dateipt.upper() == "TODAY" or dateipt == "NOW":
        now = datetime.datetime.now()
    else:
        now = datetime.datetime.strptime(dateipt, "%Y%m%d")
except ValueError:
    print("ERROR 00: 날짜 형식이 잘못되었습니다.")
    exit()

if dateipt.upper() == "NOW":
    t = now.hour
    if t <= 8:
        t = 0
    elif t <= 12:
        t = 1
    elif t <= 19:
        t = 2
    else:
        t = 0
        now += datetime.timedelta(1)
else:
    t = input("아침, 점심, 저녁 중 무엇을 알고 싶으신가요? : ")

    if t == "아침":
        t = 0
    elif t == "점심":
        t = 1
    elif t == "저녁":
        t = 2

# format the date to YYYYMMDD
date = now.strftime("%Y%m%d")


url = str.format(
    "https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=ec86c034134b4479bcbdf413fa3f2288&Type=json&ATPT_OFCDC_SC_CODE=R10&SD_SCHUL_CODE=8750767&MLSV_YMD={0}",
    date,
)


# get a text from the url
text = rq.get(url).text

# if text is json, parse it
if text.startswith("{"):
    text = pd.read_json(StringIO(text))

# if text is xml, parse it
elif text.startswith("<"):
    text = pd.read_xml(text)

# if text is not a formatted text, throw exception
else:
    raise Exception("ERROR 01: 문자열이 올바르지 않습니다. 나중에 다시 시도해주세요.")

# # print the text as full table (not truncated or ellipsed)
# pd.set_option("display.max_colwidth", None)
# print(text)


try:
    # print the DDISH_NM in the text
    food = text["mealServiceDietInfo"][1]["row"][t]["DDISH_NM"]
except:
    food = "급식 없음"


# substitute the <br/> with \n
food = food.replace("<br/>", "\n")

# clear console

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

cl = ai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "당신은 객관적으로 급식의 맛을 평가하는 인공지능입니다. 0부터 100까지의 숫자로 평가 점수를 반환하세요. 숫자 이외에 다른 문자를 포함하면 안 됩니다.\n평가는 고기, 디저트, 카레, 튀김 등의 맛있는 음식이 많을 경우 점수가 올라갑니다.\n생선이 포함된 음식이나 해산물, 채소가 많을 경우 점수가 내려갑니다.",
        },
        {
            "role": "user",
            "content": str.format("다음은 오늘의 학교 급식이야. 평가해 줘:\n{0}", food),
        },
    ],
)


print(
    str.format(
        "===== {0}년 {1}월 {2}일의 {3} 급식 메뉴 =====",
        now.year,
        now.month,
        now.day,
        "아침" if t == 0 else "점심" if t == 1 else "저녁",
    )
)
print(food)

if food != "급식 없음":
    print("---------------------------------------------")
    print(str.format("GPT 피셜 오늘의 G-Score: {0}점", cl.choices[0].message.content))
print("=============================================")

input("종료하려면 Enter를 누르십시오.")
