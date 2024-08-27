import re

q = re.findall(r"What is[a-z ,;'\-]*\?", input())
q = [re.sub(r"What(?P<question>.*)\?", r"Forty-two\g<question>.", s) for s in q]

for i in q:
    print(i)
