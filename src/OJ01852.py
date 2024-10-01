t = int(input())
ans = []
for i in range(t):
    pole_length, n = map(int, input().split())
    position = list(map(int, input().split()))
    position.sort()
    longest = max(position[-1], pole_length-position[0])
    shortest = -1
    for i in range(n-1):
        if position[i] <= pole_length/2 <= position[i + 1]:
            shortest = max(position[i], pole_length-position[i+1])
    if shortest == -1:
        shortest = min(position[-1], pole_length-position[0])
    ans.append(f"{shortest} {longest}")
for i in ans:
    print(i)