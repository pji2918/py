letter = ("A", "B", "C")
number = ("1", "2")

seats = list()

for i in letter:
    for ii in number:
        seats.append(f"{i}{ii}")

print(seats)
