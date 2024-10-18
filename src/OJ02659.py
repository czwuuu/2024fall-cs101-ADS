A, B, K = map(int, input().split())
board = [[1]*(B) for _ in range(A)]
for _ in range(K):
    R, S, P, T = map(int, input().split())
    for i in range(max(0, R-1-(P-1)//2), min(A, R+(P-1)//2)):
        for j in range(max(0, S-1-(P-1)//2), min(B, S+(P-1)//2)):
                if T == 1:
                    board[i][j] += 1
                else:
                    board[i][j] = 0
max_num = 0
max_count = 0
for i in range(A):
    for j in range(B):
        if board[i][j]>max_num:
            max_num = board[i][j]
            max_count = 1
        elif board[i][j]==max_num:
            max_count += 1
print(max_count)