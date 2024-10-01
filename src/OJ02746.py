ans = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        monkeys = [i+1 for i in range(n)]
        last_del = 0
        for _ in range(n-1):
            last_del = (m+last_del-1) % len(monkeys)
            del monkeys[last_del]
        ans.append(monkeys[0])
for item in ans:
    print(item)