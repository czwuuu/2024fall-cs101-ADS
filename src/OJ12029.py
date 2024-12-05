from collections import deque

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(xw, yw, field, I, J):
    queue = deque(); queue.append((xw, yw))
    if xw == I and yw == J:
        return True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if field[nx][ny] < field[x][y]:
                field[nx][ny] = field[x][y]
                if nx == I and ny == J:
                    return True
                queue.append((nx, ny))
    return False


k = int(input())
answer = []
for _ in range(k):
    #input
    M, N = map(int, input().split())
    field = [[99999]*(N+2)]+[[99999]+list(map(int, input().split()))+[99999] for _ in range(M)]+[[99999]*(N+2)]
    I, J = map(int, input().split())
    P = int(input())
    ans = False

    #process
    for _ in range(P):
        xw, yw = map(int, input().split())
        ans = bfs(xw, yw, field, I, J)
        if ans:
            break
    answer.append(ans)

for a in answer:
    print('Yes' if a else 'No')
