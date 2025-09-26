import random

count = 0
number = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞추시오")
while True:
    count += 1
    user_guess = int(input("숫자를 입력하시오: "))
    if user_guess == number:
        print(f"축하합니다. 총 시도횟수 = {count}")
        break
    elif user_guess < number:
        print("낮음!")
    else:
        print("높음!")
