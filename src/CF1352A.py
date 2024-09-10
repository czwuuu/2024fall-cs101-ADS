t = int(input())
k = [0]*t
ans = []
for i in range(t):
    n_str = input()
    for j in range(len(n_str)):
        if n_str[j] != "0":
            k[i] += 1
            ans.append(n_str[j]+"0"*(len(n_str)-j-1))

count = 0
for i in range(t):
    print(k[i])
    print(*ans[count:(count+k[i])])
    count += k[i]

