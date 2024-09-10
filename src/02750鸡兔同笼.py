foot = int(input())
if foot%2 == 0 :
    max = foot/2
    if foot%4 == 0 :
        min = foot/4
    else :
        min = (foot/2+1)/2
    min = int(min)
    max = int(max)
    print(min, max)
else :
    print(0, 0)
