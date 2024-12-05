t = int(input())
s = list(map(int, input().split()))
s.sort()
i = 0
j = len(s)-1
dual = False
an_list = [s[i]+s[j]]
while i+1 < j:
    if s[i]+s[j] == t:
        an_list.append(t)
        break
    elif s[i]+s[j] < t:
        i += 1
        an_list.extend([s[i]+s[j]])
    elif s[i]+s[j] > t:
        j -= 1
        an_list.extend([s[i]+s[j]])
an_list.sort(key = lambda x: (abs(x-t), x))
print(an_list[0])