def seven_related(x):
    x_str = str(x)
    if x % 7 == 0 or "7" in x_str:
        return True
    else:
        return False

n = int(input())
nums = [i**2 for i in range(1,n+1) if not(seven_related(i))]
print(sum(nums))