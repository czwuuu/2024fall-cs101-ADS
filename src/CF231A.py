sol = 0
n = int(input())
for i in range(n) :
    var = list(map(int, input().split()))
    if sum(var) >= 2 :
        sol += 1
print(sol)