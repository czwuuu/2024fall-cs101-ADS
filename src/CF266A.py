n = int(input())
s = list(input())
result = 0
i = 1
while i < len(s):
    if s[i-1] == s[i]:
        del s[i]
        result += 1
    else:
        i += 1
print(result)