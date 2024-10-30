tot = int(input())  # 책의 총 가격
p = []  # 책의 가격들을 저장할 리스트

for _ in range(9):  # 9권의 책 가격을 입력받음
    p.append(int(input()))  # 리스트에 책 가격 추가

print(tot - sum(p))  # 총 가격에서 9권의 책 가격을 빼서 출력
