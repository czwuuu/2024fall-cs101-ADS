t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tup_li = [(a[i], b[i]) for i in range(n)]
    tup_li.sort(reverse=True)
    petya_time = 0
    pointer = 0
    while pointer < n:
        if (tup_li[pointer][0]-tup_li[pointer][1]) >= petya_time:
            petya_time += tup_li[pointer][1]
            pointer += 1
        else:
            break
    answer.append(max(petya_time, tup_li[pointer][0] if pointer < n else 0))
for ans in answer:
    print(ans)