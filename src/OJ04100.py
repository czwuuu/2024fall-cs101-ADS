k = int(input())
ans = []
for _ in range(k):
    n = int(input())
    sd = [tuple(map(int, input().split())) for _ in range(n)]
    sd.sort()
    test = 1
    test_point = [sd[0][1]]
    for i in range(n):
        if sd[i][1] < test_point[test-1]:
            test_point[test-1] = sd[i][1]
        if sd[i][0] > test_point[test-1]:
            test += 1
            test_point.append(sd[i][1])
    ans.append(test)
for i in ans:
    print(i)
