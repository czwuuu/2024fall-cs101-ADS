from math import sqrt

'''弱鸡算法'''
# primes = [2, 3, 5, 7, 11, 13, 17, 19]
# for i in range(23, int(1e6)):
#     check = True
#     for prime in primes:
#         if i % prime == 0:
#             check = False
#     if check:
#         primes.append(i)
# primes = set(primes)
# print(primes)

'''eratosthenes筛法'''
# def sieve(n):
#     is_prime = [True for i in range(n+1)]
#     is_prime[0] = False
#     is_prime[1] = False
#
#     for i in range(2, int(sqrt(n))+1):
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False
#
#     primes = [i for i in range(2, n+1) if is_prime[i]]
#     return set(primes)

'''linear_sieve'''
def sieve(n):
    is_prime = [True]*(n+1)
    primes = []

    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i*p] = False
            if i % p == 0:
                break
    return set(primes)


primes = sieve(1000000)

def check_tprime(t):
    s = sqrt(t)
    if s == int(s):
        if s in primes:
            return True
        else:
            return False
    else:
        return False

n = int(input())
x = list(map(int, input().split()))
ans = []
for i in range(n):
    if check_tprime(x[i]):
        ans.append("YES")
    else:
        ans.append("NO")

for item in ans:
    print(item)