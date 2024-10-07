n = int(input())
t = list(map(int, input().split()))
t.sort()
man_happy = 1

tsum_n = [0]
sum_n = 0
for j in range(n):
    sum_n += t[j]
    tsum_n.append(sum_n)

less = 0
for i in range(1, n):
    if tsum_n[i]-less <= t[i]:
        man_happy += 1
    else:
        less += t[i]
print(man_happy)

'''思路：先排序，若有人不满意排到最后，因为没法让他更满意了。'''
'''之后需要解决求和N^2的问题，这个之前学过。但是需要考虑把人排到最后的问题。于是引入less'''