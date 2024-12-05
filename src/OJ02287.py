
answer = []
while 1:
    n = int(input())
    if not n:
        break
    else:
        tianji = list(map(int, input().split()))
        king = list(map(int, input().split()))
        tianji.sort(); king.sort()
        ans = 0
        while tianji and king:
            if tianji[0] > king[0]:
                ans += 1
                del tianji[0], king[0]
            elif tianji[-1] > king[-1]:
                ans += 1
                del tianji[-1], king[-1]
            else:
                if tianji[0] < king[-1]:
                    ans -= 1
                del tianji[0], king[-1]
        answer.append(ans)
for ans in answer:
    print(ans * 200)