inp = input()

cost = int(inp.split(" ")[0])
money = int(inp.split(" ")[1])
amount = int(inp.split(" ")[2])

totalCost = 0

for i in range(1, amount + 1):
    totalCost += cost * i

needMoreCash = totalCost - money

if needMoreCash <= 0:
    needMoreCash = 0

print(needMoreCash)
