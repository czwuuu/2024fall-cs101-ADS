def gcd(x, y): #默认 x <= y
    while y % x != 0:
        y = y % x
        x, y = y, x
    return x


ans = []
while True:
    try:
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        ans.append(gcd(x, y))
    except EOFError:
        for item in ans:
            print(item)
        break