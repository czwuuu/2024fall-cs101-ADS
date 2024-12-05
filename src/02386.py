# import sys
# sys.setrecursionlimit(100000)
#
# width_step = [-1, 0, 1]
# height_step = [-1, 0, 1]
# def dfs(x, y, field):
#     field[x][y] = '.'
#     for dx in width_step:
#         for dy in height_step:
#             if field[x+dx][y+dy] == 'W':
#                 dfs(x+dx, y+dy, field)
#
# N, M = map(int, input().split())
# field = [['.']*(M+2)]
# for _ in range(N):
#     field.append(['.']+list(input())+['.'])
# field.append(['.']*(M+2))
#
# cnt = 0
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         if field[i][j] == 'W':
#             cnt += 1
#             dfs(i, j, field)
# print(cnt)

#bfs实现
dxs = [-1, 0, 1]
dys = [-1, 0, 1]

def bfs(x, y, field):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        field[x][y] = '.'
        for dx in dxs:
            for dy in dys:
                nx, ny = x+dx, y+dy
                if field[nx][ny] == 'W':
                    queue.append((nx, ny))

N, M = map(int, input().split())
field = [['.']*(M+2)]
for _ in range(N):
    field.append(['.']+list(input())+['.'])
field.append(['.']*(M+2))

cnt = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if field[i][j] == 'W':
            cnt += 1
            bfs(i, j, field)
print(cnt)