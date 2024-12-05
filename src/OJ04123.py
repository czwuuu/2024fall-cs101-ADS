directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
def dfs(field, x, y, res_pos, routes = 0):
    if res_pos == 0:
        routes += 1
        return routes
    for i in range(8):
        nx, ny = x + directions[i][0], y + directions[i][1]
        if field[nx+1][ny+1] == 0:
            field[nx+1][ny+1] = 1
            routes = dfs(field, nx, ny, res_pos-1, routes)
            field[nx+1][ny+1] = 0
    return routes

t = int(input())
answer = []
for _ in range(t):
    n, m, x, y = map(int, input().split())

    field = [[1]*(m+4) for _ in range(2)]
    field = field + [[1, 1]+[0]*m+[1, 1] for _ in range(n)]
    field = field + [[1]*(m+4) for _ in range(2)]

    field[x+2][y+2] = 1
    routes = dfs(field, x+1, y+1, m*n-1)
    answer.append(routes)

for ans in answer:
    print(ans)