radius = int(input())
pdt = int(input())
thisUsage = int(input())
previousUsage = int(input())

mainfee = 0

if radius == 13:
    mainfee = 570
elif radius == 20:
    mainfee = 1330
elif radius == 25:
    mainfee = 2560

usage = thisUsage - previousUsage

usageFee = 0

if pdt == 1:
    if usage >= 0 and usage <= 10:
        usageFee = usage * 460
    elif usage >= 11 and usage <= 20:
        usageFee = usage * 520
    elif usage >= 21 and usage <= 30:
        usageFee = usage * 570
    elif usage >= 31 and usage <= 40:
        usageFee = usage * 710
    elif usage >= 41 and usage <= 50:
        usageFee = usage * 860
    else:
        usageFee = usage * 990
elif pdt == 2:
    if usage >= 0 and usage <= 20:
        usageFee = usage * 970
    elif usage >= 21 and usage <= 50:
        usageFee = usage * 1000
    elif usage >= 51 and usage <= 100:
        usageFee = usage * 1080
    elif usage >= 101 and usage <= 300:
        usageFee = usage * 1250
    else:
        usageFee = usage * 1670

totalFee = mainfee + usageFee

print(totalFee)
