n = int(input())
ans = []
dict = {1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144,13:233,14:377,15:610,16:987,17:1597,18:2584,19:4181,20:6765}
for i in range(n):
    a = int(input())
    ans.append(dict[a])
for item in ans:
    print(item)