import fractions

st = input().split(":")
num = fractions.Fraction(int(st[0]), int(st[1]))

print(str(num.numerator) + ":" + str(num.denominator))
