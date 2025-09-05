height = float(input("키 입력(cm): "))
weight = float(input("몸무게 입력(kg): "))

bmi = weight / (height / 100) ** 2
print(bmi)
