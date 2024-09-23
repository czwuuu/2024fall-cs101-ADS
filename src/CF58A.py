s = input()
count = 0
target_word = "hello"
ans = "NO"
for i in range(len(s)):
    if s[i] == target_word[count]:
        count += 1
        if count == 5:
            ans = "YES"
            break
print(ans)