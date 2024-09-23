A = []
B = []
C = []
ax, ay = map(int, input().split())
for i in range(ax):
    A.append(list(map(int, input().split())))
bx, by = map(int, input().split())
for i in range(bx):
    B.append(list(map(int, input().split())))
cx, cy = map(int, input().split())
for i in range(cx):
    C.append(list(map(int, input().split())))

if not(ay == bx and ax == cx and by == cy):
    print("Error!")
else:
    result = [[0]*cy for _ in range(cx)]
    for i in range(cx):
        for j in range(cy):
            for k in range(ay):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] += C[i][j]

    for i in range(cx):
        print(" ".join(map(str,result[i])))

