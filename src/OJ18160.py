dxs = [-1, 0, 1]; dys = [-1, 0, 1]
def dfs(field, x, y, area = 1):
    for dx in dxs:
        for dy in dys:
            nx, ny = x+dx, y+dy
            if field[nx][ny] == 'W':
                field[nx][ny] = '.'
                area += 1
                area = dfs(field, nx, ny, area)
    return area


t = int(input())
answer = []
for _ in range(t):
    n, m = map(int, input().split())
    largest_area = 0
    field = [['.']*(m+2)]
    field = field+[['.']+list(input())+['.'] for _ in range(n)]
    field = field+[['.']*(m+2)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if field[i][j] == 'W':
                field[i][j] = '.'
                this_area = dfs(field, i, j)
                if this_area > largest_area:
                    largest_area = this_area
    answer.append(largest_area)
for ans in answer:
    print(ans)
