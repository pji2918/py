import random
import tools.putil as putil

questions = []
for i in range(10):
    questions.append(putil.getStatement(min=1, max=3000))

q = random.choice(questions)
print(f"{q} = {eval(q)}")
