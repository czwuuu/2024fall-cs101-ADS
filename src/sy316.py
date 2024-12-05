direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(field, x, y):
    global val, mval
    global final_route
    for i in range(4):
        nx, ny = x+direction[i][0], y+direction[i][1]
        if nx == n and ny == m:
            route.append((n, m))
            if val + value[n][m] > mval:
                mval = val + value[n][m]
                final_route = route[:]
            route.pop()
            continue
        if field[nx][ny] == 0:
            val += value[nx][ny]
            route.append((nx, ny))
            field[nx][ny] = 1
            dfs(field, nx, ny)
            field[nx][ny] = 0
            route.pop()
            val -= value[nx][ny]
    return


n, m = map(int, input().split())

value = [[1]*(m+2)]
value = value+[[1]+list(map(int, input().split()))+[1] for _ in range(n)]
value = value+[[1]*(m+2)]
field = [[1]*(m+2)]+[[1]+[0]*m+[1] for _ in range(n)]+[[1]*(m+2)]

field[1][1] = 1
final_route = []
route = [(1, 1)]
val = value[1][1]; mval = float('-inf')

dfs(field, 1, 1)
for point in final_route:
    print(*point)