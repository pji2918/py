a = input("a = ")
b = input("b = ")

new_str1 = ""
new_str2 = ""

for i, ii in zip(a, b):
    new_str1 += f"{i}{ii}"
for i, ii in zip(a, reversed(b)):
    new_str2 += f"{i}{ii}"

print(f"new_str1 = {new_str1}")
print(f"new_str2 = {new_str2}")
