ans = "NO"
players = list(input())
count = 0
for i in range(len(players)-1):
    if players[i+1] == players[i]:
        count += 1
        if count == 6:
            ans = "YES"
    else:
        count = 0
print(ans)