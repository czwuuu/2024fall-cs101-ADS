n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
b.sort()
match = 0

i = 0
last_girl = 0
while i < n:
    j = last_girl
    while j < m:
        if abs(a[i]-b[j]) <= 1:
            match += 1
            last_girl = j+1
            i += 1
        if i == n:
            break
        j += 1
    i += 1

print(match)

'''greedy，虽然没有严格证明，但感觉上是对的。也是看了提示'''