d = int(input())
n = int(input())
board = [[0]*1025 for _ in range(1025)]
for _ in range(n):
    x, y, i = map(int, input().split())
    for j in range(max(0, x-d), min(1025, x+d+1)):
        for k in range(max(0, y-d), min(1025, y+d+1)):
            board[j][k] += i
Max_num = 0
point_cnt = 0
for j in range(1025):
    for k in range(1025):
        if board[j][k] > Max_num:
            Max_num = board[j][k]
            point_cnt = 1
        elif board[j][k] == Max_num:
            point_cnt += 1
print(point_cnt, Max_num)
