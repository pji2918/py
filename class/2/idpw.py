ac = {"ilovepython": "mypass1234", "chicken": "chickenisDelicious"}

id = input("아이디를 입력하시오: ")
pw = input("패스워드를 입력하시오: ")

# if id in ac:
#     if pw == ac[id]:
#         print("환영합니다.")
#     else:
#         print("비밀번호가 틀렸습니다.")
# else:
#     print("아이디를 찾을 수 없습니다.")
if id in ac and pw == ac[id]:
    print("환영합니다.")
else:
    print("아이디 또는 비밀번호가 일치하지 않습니다.")
