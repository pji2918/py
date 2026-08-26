#!/usr/bin/env python

import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--verbose", help="show detailed debug info", action="store_true"
)
args = parser.parse_args()

while True:
    mode = input("모드를 입력하십시오(한글, 노한글, 자음모음한글, 모두): ")

    if mode == "한글" or mode == "hangul":
        randstr = [chr(i) for i in range(0xAC00, 0xD7A4)]
    elif mode == "노한글" or mode == "nohangul":
        randstr = string.ascii_letters + string.digits + string.punctuation
    elif mode == "자음모음한글" or mode == "jamohangul":
        randstr = f"{[chr(i) for i in range(0xAC00, 0xD7A4)]}{[chr(i) for i in range(0x3131, 0x3163)]}"
    elif mode == "모두" or mode == "all":
        randstr = f"{string.ascii_letters}{string.digits}{string.punctuation}{[chr(i) for i in range(0xAC00, 0xD7A4)]}{[chr(i) for i in range(0x3131, 0x3163)]}"
    else:
        print('그런 모드는 존재하지 않는다. 그냥 "모두"를 사용하겠다.')
        randstr = f"{string.ascii_letters}{string.digits}{string.punctuation}{[chr(i) for i in range(0xAC00, 0xD7A4)]}{[chr(i) for i in range(0x3131, 0x3163)]}"

    iteration = int(input("뽑을 글자 수를 입력하십시오: "))

    try:
        for i in range(iteration):
            print(random.choice(randstr), end="")

        print("\n완료. 다시 하시겠습니까?")
        ans = input("답(y/n): ")

        if ans.lower() == "y" or "ㅇ" in ans:
            continue
        elif ans.lower() == "n" or "ㄴ" in ans:
            break
    except ValueError, TypeError:
        print("Error. 해당 값은 입력할 수 없습니다.")
        continue
