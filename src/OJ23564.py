def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input())
ans = 0
factors = prime_factors(n)
if len(factors) == len(set(factors)):
    if len(factors) % 2 == 0:
        ans = 1
    else:
        ans = -1

print(ans)