pika = ["pi", "ka", "chu"]

a = input()
for i in pika:
    if i in a:
        a = a.replace(i, "-")

isNothasPika = True
for i in a:
    if i != "-":
        isNothasPika = False

if isNothasPika:
    print("YES")
else:
    print("NO")
