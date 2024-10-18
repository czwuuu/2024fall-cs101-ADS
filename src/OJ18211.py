p = int(input())
price = list(map(int, input().split()))

price.sort()
i = -1; j = len(price)

weapon_num_d = 0

while i+1 != j:
    if p - price[i+1] >= 0:
        i += 1
        p -= price[i]
    elif (i+1) >= len(price)-(j-1):
        weapon_num_d = max(weapon_num_d, i+1-len(price)+j)
        j -= 1
        p += price[j]
    else:
        weapon_num_d = max(weapon_num_d, i + 1 - len(price) + j)
        break

weapon_num_d = max(weapon_num_d, i + 1 - len(price) + j)
print(weapon_num_d)