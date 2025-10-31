import string

txt = input("문장을 입력하시오 : ")
shift = int(input("이동시킬 칸 수를 입력하시오 : "))

srcTable = string.ascii_uppercase + string.ascii_lowercase
encTable = (
    string.ascii_uppercase[shift:]
    + string.ascii_uppercase[:shift]
    + string.ascii_lowercase[shift:]
    + string.ascii_lowercase[:shift]
)

encrypted_text = ""

for i in txt:
    if i.isalpha():
        encrypted_text += encTable[srcTable.index(i)]
    else:
        encrypted_text += i

print(f"암호화된 문장: {encrypted_text}")
