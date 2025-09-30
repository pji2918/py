def cel2fah(celsius):
    return (9 / 5) * celsius + 32


for i in range(0, 51, 10):
    print(f"{i} => {cel2fah(i)}")
