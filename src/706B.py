n = int(input())
x = list(map(int, input().split()))
q = int(input())
coins = [int(input()) for _ in range(q)]

shops_avl = {}
coins_and_day = [(coins, day) for day, coins in enumerate(coins)]

x.sort()
coins_and_day.sort()

i = 0

#gpt帮忙做的逻辑简化，以及变量解包
for j in range(q):
    coin, day = coins_and_day[j]
    while i < n and coin >= x[i]:
        i += 1
    shops_avl[day] = i


for i in range(q):
    print(shops_avl[i])