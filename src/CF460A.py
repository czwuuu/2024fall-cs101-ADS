n, m = map(int, input().split())
days = 0
count = 0
while n > 0:
    days += 1
    n -= 1
    count += 1
    if count == m:
        n += 1
        count = 0
print(days)