import sys
sys.setrecursionlimit(1<<30)

n = int(input())
permutation = list(map(int, input().split()))

def sort_and_inversion(seq):
    cnt = 0
    mid = len(seq)//2
    if mid < 1:
        return seq, 0

    left, a = sort_and_inversion(seq[:mid])
    right, b = sort_and_inversion(seq[mid:])
    cnt += a+b
    return merge(left, right, cnt)

def merge(left, right, cnt):
    result = []
    i = 0; j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            cnt += j
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:]+right[j:])
    cnt += (len(left)-i)*len(right)
    return result, cnt

result, cnt = sort_and_inversion(permutation)
print(cnt)
