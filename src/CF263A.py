matrix = []
row = 0
col = 0
for i in range(5):
    alist = list(map(int, input().split()))
    matrix.append(alist)
    if 1 in alist:
        row = i + 1
        col = alist.index(1) + 1
result = abs(3-row) + abs(3-col)
print(result)