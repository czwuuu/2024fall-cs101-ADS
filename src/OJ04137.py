t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, input().split())
    n = list(map(int, list(str(n))))
    stack = [0]
    i = 0
    while k > 0:
        if n[i] >= stack[-1] or i == 0:
            stack.append(n[i])
            i += 1
            if i == len(n):
                break
        else:
            stack.pop()
            del n[i-1]
            i -= 1
            k -= 1
    if k > 0 and i == len(n):
        n = n[:(len(n)-k)]
    answer.append(''.join(map(str, n)))

for ans in answer:
    print(ans)