N = int(input())
factor = 6
gcd = 0
while True:
    if N%factor == 0:
        gcd = N/factor
        break
    else:
        factor += 1
print(int(gcd))