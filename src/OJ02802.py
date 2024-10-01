#connect, 能连接返回segments, 不能连接返回0
def connect(mat, w, h, x1, y1, x2, y2):
    segments = 0
    x1 = x1 + 1
    y1 = y1 + 1
    x2 = x2 + 1
    y2 = y2 + 1
    direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    dir_ind = 0
    while not(x1 == x2 and y1 == y2):
        x1 += direction[dir_ind][0]
        y1 += direction[dir_ind][1]
        if mat[y1][x1] == "X" or x1 < 0 or x1 > w+1 or y1 < 0 or y1 > h+1:
            x1 -= direction[dir_ind][0]
            y1 -= direction[dir_ind][1]
            dir_ind += 1
            if dir_ind == 4:
                segments = 0
                break

    return segments

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

#输出模块
for i in range(1, n):
    print(f"Board #{i}:")
    for j in range(1, m):
        if answer[i-1][j-1] == 0:
            ans_word = "impossible."
        else:
            ans_word = str(answer[i-1][j-1])+" segments."
        print(f"Pair {j}: {ans_word}")