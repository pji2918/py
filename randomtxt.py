import random
import string

# randstr = (string.ascii_letters + string.digits).join(
#     [chr(i) for i in range(0xAC00, 0xD7A4)]
# )

while True:
    randstr = "".join([chr(i) for i in range(0xAC00, 0xD7A4)])

    iteration = input("뽑을 글자 수를 입력하십시오: ")

    try:
        for i in range(int(iteration)):
            print(random.choice(randstr), end="")
        break
    except (ValueError, TypeError):
        print("Error. 숫자만 입력할 수 있습니다.")
        continue
