from time import time
time_start = time()

nums = list(map(int, input().split(",")))
k = int(input())
multiplier = int(input())

def exp_mod(a, n, m):  # b^n%m
    n_bin = bin(n)[2:]
    table = [a]
    ret = 1
    for j in range(len(n_bin) - 1):
        var_app = (table[j] ** 2) % m
        table.append(var_app)
    for j in range(len(n_bin)):
        if n_bin[len(n_bin) - 1 - j] == "1":
            ret = ret * table[j] % m
    return ret

time1 = time()

mod = 10 ** 9 + 7
b = k
for i in range(k):
    min_ind = nums.index(min(nums))
    max_val = max(nums)
    nums[min_ind] = nums[min_ind] * multiplier
    if nums[min_ind] >= max_val:
        b = i + 1
        if (k - b) % (len(nums)) == 0:
            break

time2 = time()

exp = int((k - b) / len(nums))
mul = exp_mod(multiplier, exp, mod)
nums_mod = [x * mul % mod for x in nums]

time3 = time()

print(nums_mod)
print(time3-time2, time2-time1)