import re

ip = input("IP 주소를 입력하시오 : ")

if re.match(r"^(((?!25?[6-9])[12]\d|[1-9])?\d\.?\b){4}$", ip):
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")
