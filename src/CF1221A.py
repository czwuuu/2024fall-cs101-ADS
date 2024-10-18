from collections import Counter
q = int(input())
answer = []

for i in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    s_counted = Counter(s)
    for i in range(0, 11):
        s_counted[2**(i+1)] = s_counted.get(2**(i+1), 0) + s_counted.get(2**i, 0)//2
    answer.append(1 if s_counted[2048] > 0 else 0)

for i in answer:
    print("YES" if i else "NO")