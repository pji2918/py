def c2f(celsius):
    return (9 / 5) * celsius + 32


print("섭씨\t화씨")
print("=" * 13)
for i in range(0, 51, 10):
    print(f"{i:2}\t{c2f(i):5.1f}")

# celsius = float(input("섭씨온도를 입력하십시오: "))
# fahrenheit = c2f(celsius)
# print(f"섭씨 {celsius:.0f}도는 화씨 {fahrenheit:.1f}도입니다.")
