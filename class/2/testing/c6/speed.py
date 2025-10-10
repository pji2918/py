speed = float(input("평균 시속(km/h)을 입력하세요 : "))
time = float(input("이동 시간(h)을 입력하세요 : "))
print(f"평균 시속 :  {speed} km/h")

tempTime = time
h = int(tempTime)
tempTime %= 1
m = int(tempTime * 60)
tempTime = (tempTime * 60) % 1
s = int(tempTime * 60)

print(f"이동 시간 :  {h} 시간 {m} 분 {s} 초")
print(f"이동 거리 : {speed * time} km")
