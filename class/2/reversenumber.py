while True:
    num = input("정수를 입력하시오: ")
    if num == "-99":
        break
    elif num == num[::-1]:
        print(f"{num}은(는) 거꾸로 정수입니다.")
    else:
        print(f"{num}은(는) 거꾸로 정수가 아닙니다.")
print("프로그램을 종료합니다.")
