fruit_list = ["banana", "orange", "kiwi", "apple", "melon"]

maxlen = 0

for i in fruit_list:
    if len(i) >= maxlen:
        maxlen = len(i)

removelist = []
print("가장 길이가 긴 문자열 : ", end="")
for i in range(len(fruit_list)):
    if len(fruit_list[i]) == maxlen:
        removelist.append(i)
for i in removelist:
    print(fruit_list[i], end="")
    if not removelist.index(i) == len(removelist) - 1:
        print(", ", end="")
    else:
        print()
    fruit_list.pop(i)

print(f"fruit_list = {fruit_list}")
