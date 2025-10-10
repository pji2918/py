threeDigitInteger = int(input("세 자리 정수를 입력하시오 : "))

digitOfHundred = threeDigitInteger // 100
threeDigitInteger %= 100
digitOfTen = threeDigitInteger // 10
threeDigitInteger %= 10

print(f"{threeDigitInteger}{digitOfTen}{digitOfHundred}")
