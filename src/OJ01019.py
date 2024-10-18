import bisect
t = int(input())
answer = []
length_sum = []
l_s = 0
word = ''
for li in range(1, 31300):
    word += str(li)
for k in range(0, 31268):
    if k <= 9:
        l_s += k
    elif 10 <= k <= 99:
        l_s += 9 + 2*(k-9)
    elif 100 <= k <= 999:
        l_s += 189 + 3*(k-99)
    elif 1000 <= k <= 9999:
        l_s += 2889 + 4*(k-999)
    elif k >= 10000:
        l_s += 38889 + 5*(k-9999)
    length_sum.append(l_s)
for _ in range(t):
    i = int(input())
    k = bisect.bisect_left(length_sum, i)
    i -= length_sum[k-1]
    answer.append(word[i-1])
for ans in answer:
    print(ans)