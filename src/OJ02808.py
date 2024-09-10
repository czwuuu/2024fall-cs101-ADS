L, M = map(int, input().split())
trees = [1]*(L+1)
for _ in range(M):
    start, end = map(int, input().split())
    trees[start:end+1] = [0]*(end-start+1)
result = sum(trees)
print(result)