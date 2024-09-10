n = int(input())
nums = list(map(int, input().split()))
nums = [i%2 for i in nums]
ans = 0
if nums[0] == nums[1]:
    for i in range(len(nums)):
        if nums[i] != nums[0]:
            ans = i+1
else:
    if nums[0] != nums[2]:
        ans = 1
    else:
        ans = 2
print(ans)