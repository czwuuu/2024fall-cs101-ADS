n = int(input())
v = list(map(int, input().split()))
u = sorted(v)

vsum = 0
vs = [0]
for vi in v:
    vsum += vi
    vs.append(vsum)

usum = 0
us = [0]
for ui in u:
    usum += ui
    us.append(usum)


question_number = int(input())
answer = []
for _ in range(question_number):
    type, l, r = map(int, input().split())
    if type == 1:
        ans = vs[r]-vs[l-1]
        answer.append(ans)
    else:
        ans = us[r]-us[l-1]
        answer.append(ans)
for ans in answer:
    print(ans)

'''在之前的题目中见过这种快速求列表切片和的算法，所以这道题很快解决了'''
'''每次求sum是一个很慢的过程，把求和变成两数相减，复杂度从N^2到N'''