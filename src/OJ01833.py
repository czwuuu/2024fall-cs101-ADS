# import bisect
#
# def pre_calculate_factorials(length):
#     factorials = [1]*(length+1)
#     for i in range(2, length+1):
#         factorials[i] = factorials[i-1]*i
#     return factorials
#
# def cantor_expansion(arr, factorials):
#     length = len(arr)
#     numbers = list(range(1, length+1))
#     rank = 0
#     for i in range(n):
#         index = bisect.bisect_left(numbers, arr[i])
#         rank += index*factorials[length-i-1]
#         del numbers[index]
#     return rank
#
# def inverse_cantor_expansion(rank, length, factorials):
#     arr = []
#     elements = list(range(1, length+1))
#     for i in range(length, 0, -1):
#         index = rank // factorials[i-1]
#         arr.append(elements.pop(index))
#         rank %= factorials[i-1]
#     return arr
#
# m = int(input())
# answer = []
# for _ in range(m):
#     n, k = map(int, input().split())
#     this_factorials = pre_calculate_factorials(n)
#     arrange = list(map(int, input().split()))
#     rank_ = cantor_expansion(arrange, this_factorials)
#     rank_ = (rank_+k)%this_factorials[n]
#     answer.append(inverse_cantor_expansion(rank_, n, this_factorials))
# for ans in answer:
#     print(*ans)

""" new_algorithm """
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

m = int(input())
answer = []
for _ in range(m):
    n, k = map(int, input().split())
    permutation =  list(map(int, input().split()))
    k %= factorial(n)
    for _ in range(k):
        if permutation == list(range(n, 0, -1)):
            permutation = list(range(1, n+1))
        else:
            next_permutation(permutation)
    answer.append(permutation)
for ans in answer:
    print(*ans)

