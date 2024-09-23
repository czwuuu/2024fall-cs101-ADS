words = input().lower()
ans = []
vowels = "aoyeui"
for word in words:
    if word not in vowels:
        ans.append("."+word)
print("".join(ans))
