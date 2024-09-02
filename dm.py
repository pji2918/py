import base64
import pyperclip

pyperclip.copy(
    base64.b64encode(
        "추정: 프로젝트도 아직 안 만들었을 가능성 99% 이상.".encode()
    ).decode()
)
