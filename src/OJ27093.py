N, D = map(int, input().split())
h = list(map(int, input().split()))
hArranged = []

while h:
    free_mark = [False]*len(h)
    Max = float(h[0])
    Min = float(h[0])
    for i in range(len(h)):
        if abs(h[i]-Max) <= D and abs(h[i]-Min) <= D:
            free_mark[i] = True
        if h[i] > Max:
            Max = h[i]
        if h[i] < Min:
            Min = h[i]
    new_h = []
    ap = []
    for i in range(len(h)):
        if free_mark[i]:
            ap.append(h[i])
        else:
            new_h.append(h[i])
    ap.sort()
    h = new_h[:]
    hArranged.extend(ap)

print(*hArranged)