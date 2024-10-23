from math import sqrt, ceil
n, k = map(int, input().split())
if k > n**2:
    print(-1)
else:
    matrix = [[1]*n for _ in range(n)]
    r = int(ceil(sqrt(n**2-k)))
    k -= int(n**2-r**2)
    this_mat = [[0]*r for _ in range(r)]
    if k != 0:
        if k % 2 == 0:
            this_mat[1][1] = 1
        else:
            k += 1
        for j in range(0, k//2):
            this_mat[0][j] = 1
        for j in range(0, k//2):
            this_mat[j][0] = 1

    for i in range(n-r, n):
        for j in range(n-r, n):
            matrix[i][j] = this_mat[i-(n-r)][j-(n-r)]
    for row in matrix:
        print(*row)