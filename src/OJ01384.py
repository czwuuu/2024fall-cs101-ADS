def piggy_bank(tot_weight, coins):
    if not tot_weight:
        return 0
    dp = [0] + [-1]*tot_weight
    for i in range(1, tot_weight+1):
        available = [j for j in range(len(coins)) if i-coins[j][1] >= 0 and dp[i-coins[j][1]] > -1]
        dp[i] = min([dp[i-coins[j][1]]+coins[j][0] for j in available]) if available else -1
    return dp[-1]

t = int(input())
answer = []
for _ in range(t):
    E, F = map(int, input().split())
    N = int(input())
    coins = []
    for _ in range(N):
        coins.append(tuple(map(int, input().split())))   #value, weight
    answer.append(piggy_bank(F-E, coins))

for ans in answer:
    if ans == -1:
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {int(ans)}.')