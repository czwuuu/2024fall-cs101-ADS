n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]
if n >= 2:
    status = [0]+[1 for _ in range(n-2)]+[0]
    cut_down = 2
    segments = [trees[i+1][0]-trees[i][0] for i in range(n-1)]
    for i in range(n-1):
        if segments[i] > trees[i][1]+trees[i+1][1]:
            cut_down += status[i]+status[i+1]
            status[i] = 0
            status[i+1] = 0
        elif min(trees[i][1], trees[i+1][1]) < segments[i] <= trees[i][1]+trees[i+1][1]:
            if status[i] == 1 and segments[i] > trees[i][1]:
                cut_down += status[i]
                status[i] = 0
            elif segments[i] > trees[i+1][1]:
                cut_down += status[i+1]
                status[i+1] = 0
    print(cut_down)
else:
    print(n)