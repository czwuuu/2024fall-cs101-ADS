from collections import deque
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
step = 0

def bfs(field):
    global step

    if field[1][1] == 1:
        step = 0
        return
    queue = [(1, 1)]; field[1][1] = 2
    while queue:
        buffer = deque(queue)
        queue = []
        step += 1
        while buffer:
            x, y = buffer.popleft()
            for i in range(4):
                nx, ny = x+direction[i][0], y+direction[i][1]
                if field[nx][ny] == 1:
                    return
                elif field[nx][ny] == 0:
                    field[nx][ny] = 2
                    queue.append((nx, ny))
    step = 'NO'


m, n = map(int, input().split())

field = [[2]*(n+2)]
field = field + [[2]+list(map(int, input().split()))+[2] for _ in range(m)]
field = field + [[2]*(n+2)]

bfs(field)
print(step)