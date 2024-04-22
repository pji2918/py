def GetJongsung(cha):
    return chr(int(ord(cha) % 28))


def GetJungSung(cha):
    return chr(int(((ord(cha) - ord(GetJongsung(cha))) / 28) % 21))


def GetChosung(cha):
    return chr(
        int(((ord(cha) - ord(GetJongsung(cha))) / 28 - ord(GetJungSung(cha))) / 21)
    )


name = input()

for i in name:
    print(GetChosung(i), "")
