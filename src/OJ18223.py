m = int(input())
ans = []

for _ in range(m):
    a, b, c, d = map(int, input().split())

    # 计算所有可能的结果并存入集合
    results = set()
    for sign_a in (1, -1):
        for sign_b in (1, -1):
            for sign_c in (1, -1):
                for sign_d in (1, -1):
                    result = sign_a * a + sign_b * b + sign_c * c + sign_d * d
                    results.add(result)

    # 判断是否存在结果为 24
    if 24 in results:
        ans.append("YES")
    else:
        ans.append("NO")

# 输出结果
print("\n".join(ans))
