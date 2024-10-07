S = int(input())
a = int(S/2)

is_prime = [True]*10001
is_prime[1] = False
for i in range(2, 10001):
    if is_prime[i]:
        for num in range(i*i, 10001, i):
            is_prime[num] = False

result = 0
while not(result):
    if is_prime[a] and is_prime[S-a]:
        result = a*(S-a)
    else:
        a -= 1

print(result)

'''标志着熟练掌握埃氏筛，虽然欧拉筛还是不太会'''