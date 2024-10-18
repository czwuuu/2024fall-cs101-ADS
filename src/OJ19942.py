m, n, p, q = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]
kernel = [list(map(int, input().split())) for _ in range(p)]
answer = [[0]*(n+1-q) for _ in range(m+1-p)]

for i in range(m+1-p):
    for j in range(n+1-q):
        for k in range(p):
            for l in range(q):
                answer[i][j] += array[i+k][j+l]*kernel[k][l]
for ans in answer:
    print(*ans)