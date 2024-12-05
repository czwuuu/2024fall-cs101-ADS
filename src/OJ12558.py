n, m = map(int, input().split())
field = [[0]*(m+2)]
for _ in range(n):
    field.append([0]+list(map(int, input().split()))+[0])
field.append([0]*(m+2))

dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if field[i][j] == 1:
            cnt += 4
            for k in dxdy:
                cnt -= field[i+k[0]][j+k[1]]
print(cnt)
