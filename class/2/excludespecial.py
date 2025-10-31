import re

txt = input("입력: ")

result = re.sub(r"[^\w]", "", txt)
print(result)
