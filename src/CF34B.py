n, m = map(int, input().split())
a = list(map(int, input().split()))

ans_list = [-k for k in a if k < 0]
ans_list.sort(reverse = True)
ans = sum(ans_list)
if m < len(ans_list):
    ans = sum(ans_list[0:m])
print(ans)