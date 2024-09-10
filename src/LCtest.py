mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = []
m = len(mat)
n = len(mat[0])
print(m, n)
for s in range(m+n-1):
    if s % 2 == 0:
        final2 = min([n-1, s])
        init2 = s - min([m-1, s])
        for i in range(init2, final2 + 1):
            ans.append(mat[s-i][i])
    else:
        final1 = min([m-1, s])
        init1 = s - min([n-1, s])
        for i in range(init1, final1 + 1):
            ans.append(mat[i][s-i])
print(ans)