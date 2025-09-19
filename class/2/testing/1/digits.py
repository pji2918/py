threeDigitInteger = int(input("세 자리 정수를 입력하시오 : "))

print(f"백의 자리 : {threeDigitInteger // 100}")
threeDigitInteger %= 100
print(f"십의 자리 : {threeDigitInteger // 10}")
threeDigitInteger %= 10
print(f"일의 자리 : {threeDigitInteger // 1}")
