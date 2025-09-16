import math  # 각종 수식 계산에 필요.
import sys
import cv2  # 이미지를 처리해주는 핵심적인 라이브러리.
import numpy as np  # 이미지 연산에 필요.
import requests  # URL에서 이미지를 가져오기 위해 필요.
import turtle  # 거북이.
from time import perf_counter  # 소요 시간 측정용.


startTime = perf_counter()  # 전체 처리 시간 측정을 위해 시작 시간을 기록합니다.


def getAngle(pos1, pos2) -> float:
    """Returns angle between two vectors in degree. (Powered by Gemini because I'm Su-Po-Ja.)"""

    # x, y 변화량 계산.
    delta_x = pos2[0] - pos1[0]
    delta_y = pos2[1] - pos1[1]

    # atan2를 사용하여 라디안 각도를 계산.
    angle_radians = math.atan2(delta_y, delta_x)

    # 라디안을 도로 변환하여 반환.
    return math.degrees(angle_radians)


threshold = 300  # 감지 민감도. 높을수록 민감함.
url = "https://i.namu.wiki/i/SDMQW6pSbeK3hqI8Jw43RPuurvrTrxhL738hIV-s9EPWvyEcPBcVzF22AOOvsPoqAInexBDGyfJmst7HZJ1VpnaXaa6t7KZHNZjOzfqtSPTmAwUatHJL4OAcLapVVpWHOvIuLVHoMuJwSHmvPQrG0Q.webp"  # 변환할 이미지를 포함한 URL.

print("Requesting image...")
dl = requests.get(url)

if dl.status_code != 200:
    print("ERROR. cannot get image.")
    print(f"Error code : {dl.status_code}")
    print("Exiting.")
    sys.exit(1)

print("Processing image...")  # 이미지 처리 시작 알림 출력
img_array = np.asarray(
    bytearray(dl.content), dtype=np.uint8
)  # URL에서 이미지를 획득 후 NumPy 배열 형태로 저장.
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 배열을 OpenCV2로 디코딩.

height, width, channel = img.shape  # 이미지의 크기를 저장.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 색상 제거.
canny = cv2.Canny(
    gray, threshold, threshold * 2
)  # Canny Edge Detection Algorithm을 이용하여 가장자리 정보만 유지. 아직 이미지임.

contours, hierachy = cv2.findContours(
    canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)  # 윤곽선을 추출하여 저장.

coordinates = []  # 윤곽선의 좌표를 저장할 List 선언.

# 윤곽선 데이터를 배열에 좌표(x,y) 형태로 저장.
for i, contour in enumerate(contours):
    cord = contour.squeeze().tolist()  # contour 배열을 2D 좌표 리스트로 변환

    if isinstance(cord, int):
        continue
    if len(cord) > 1 and isinstance(cord[0], int):
        cord = [cord]

    coordinates.append(cord)  # 변환된 좌표를 전체 좌표 목록에 추가

endTime = perf_counter()  # 이미지 처리 완료 시점 기록
print(
    f"Image processing complete. Image has {len(coordinates)} line(s)."
)  # 처리 결과 요약 출력
print(f"{endTime - startTime:.2f}s elapsed.")  # 이미지 처리 소요 시간 출력.

sc = turtle.Screen()
sc.title('secondEOS == "ReallyDanger"')

t = turtle.Turtle()  # turtle 클래스 인스턴스화
t.shape("turtle")  # 거북이 모양.
t.speed(0)  # 속도 최대화


t.fillcolor("white")
startTime = perf_counter()  # 출력(거북이) 작업 시작 시간 기록
print("Printing image... (It may take a while)")  # 출력 시작 알림

t.begin_fill()
t.penup()
t.home()
t.goto(-width / 2, height / 2)
t.pendown()
t.forward(width)
t.penup()
t.goto(-width / 2, -height / 2)
t.pendown()
t.forward(width)

t.penup()
t.right(90)
t.goto(-width / 2, height / 2)
t.pendown()
t.forward(height)
t.penup()
t.goto(width / 2, height / 2)
t.pendown()
t.forward(height)
t.end_fill()

t.penup()  # 펜 올림
for i in coordinates:  # 윤곽선(한 줄씩) 반복
    t.penup()  # 펜 올림
    for ii in i:  # 한 윤곽선의 각 좌표 반복
        t.setheading(
            getAngle(t.pos(), (ii[0] - (width / 2), (height / 2) - ii[1]))
        )  # 방향 설정
        t.goto(ii[0] - (width / 2), (height / 2) - ii[1])  # 좌표로 이동
        t.pendown()  # 펜 내림
    print(
        f"Printed line {coordinates.index(i) + 1}. ({math.ceil(((coordinates.index(i) + 1) / len(coordinates)) * 100)}% complete)"
    )  # 현재까지 출력한 선의 번호와 진행률을 출력

endTime = perf_counter()  # 출력 작업 완료 시점 기록
t.hideturtle()  # 거북이 커서 숨김
print("Image print completed.")  # 출력 완료 알림
print(f"{endTime - startTime:.2f}s elapsed.")  # 출력 소요 시간 출력

input("Press Enter to exit")
