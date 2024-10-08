hangularr = [
    chr(i) for i in range(0xAC00, 0xD7A4)
]  # 한글 완성형 문자의 유니코드 범위는 0xAC00 ~ 0xD7A4이다. 이를 전부 리스트에 넣어준다.
n = int(input())  # 입력받은 숫자를 n에 저장한다.

print(hangularr[n - 1])  # n - 1번째 인덱스(n은 1부터 시작)의 한글 문자를 출력한다.
