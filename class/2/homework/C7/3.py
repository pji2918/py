list1 = ["I like", "I love"]
list2 = ["pancakes.", "kiwi juice.", "espresso."]
list3 = [f"{x} {y}" for x in list1 for y in list2]

print(list3)
print("=" * 30)
for i in list3:
    print(i)
