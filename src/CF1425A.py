def maximize(x):
    if x == 4:
        return 3
    else:
        ret = 0
        step = 0
        while x > 0:
            if step % 2 == 0:
                if x == 4:
                    ret += 3
                    x = 0
                elif (x//2) % 2 != 0:
                    ret += x//2
                    x //= 2
                elif (x//2) % 2 == 0:
                    ret += 1
                    x -= 1
            else:
                x -= 1
            step += 1
        return ret

import sys
inputs = sys.stdin.read()
data = inputs.splitlines()
data = list(map(int, data))
answer = []

for i in range(1, data[0]+1):
    n = data[i]
    coin = 0
    if n % 2 == 0:
        coin = maximize(n)
    else:
        coin = n - maximize(n-1)
    answer.append(int(coin))

sys.stdout.write('\n'.join(map(str, answer)))