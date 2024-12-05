from math import factorial
import bisect

def next_permutation(perm):
    queue = []
    while len(queue) == 0 or perm[-1] > queue[-1]:
        queue.append(perm.pop())
    insert_ele = perm.pop()
    index = bisect.bisect_left(queue, insert_ele)
    perm.append(queue[index])
    queue[index] = insert_ele
    perm.extend(queue)
    return perm

n = int(input())
k = int(input())
permutation =  list(map(int, input().split()))
k %= factorial(n)
for _ in range(k):
    if permutation == list(range(n, 0, -1)):
        permutation = list(range(1, n+1))
    else:
        next_permutation(permutation)
print(*permutation)