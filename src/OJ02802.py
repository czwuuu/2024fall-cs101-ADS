from collections import deque

direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
def connect(mat, w, h, x1, y1, x2, y2):
    queue = deque(); queue.append((x1, y1, -1, 0))
    inq = set(); inq.add((x1, y1))
    recorder = []
    if x1 == x2 and y1 == y2:
        return 0

    while queue:
        x, y, dire, turn = queue.popleft()
        for i in range(4):
            nx, ny = x+direction[i][0], y+direction[i][1]
            if (nx, ny) in inq or nx < 0 or nx > w+1 or ny < 0 or ny > h+1:
                continue
            if mat[ny][nx] != 'X' or (nx == x2 and ny == y2):
                turn_new = turn+1 if dire != i else turn
                if nx == x2 and ny == y2:
                    recorder.append(turn_new)
                else:
                    inq.add((nx, ny))
                    queue.append((nx, ny, i, turn_new))
    return min(recorder) if recorder else -1

#输入和答案的存储
n = 0
answer = []
while True:
    n += 1
    w, h = map(int, input().split())
    mat = [[" "]*(w+2)]
    if w == 0 and h == 0:
        break
    else:
        for i in range(h):
            line = [" "]+list(input())+[" "]
            mat.append(line)
        mat.append([" "]*(w+2))

        m = 0
        _answer_ = []
        while True:
            m += 1
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
                break
            else:
                _answer_.append(connect(mat, w, h, x1, y1, x2, y2))
        answer.append(_answer_)

#输出模块
for i in range(1, n):
    print(f"Board #{i}:")
    for j in range(1, len(answer[i-1])+1):
        if answer[i-1][j-1] == -1:
            ans_word = "impossible."
        else:
            ans_word = str(answer[i-1][j-1])+" segments."
        print(f"Pair {j}: {ans_word}")
    print('')