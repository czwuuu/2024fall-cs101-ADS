n = int(input())
a = list(map(int, input().split()))
dict = {}
for ai in a:
    dict[ai] = dict.get(ai, 0) + 1
visible = 0
for value in dict.values():
    if value > visible:
        visible = value
print(visible)

'''这回学会字典了'''