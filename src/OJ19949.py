n = int(input())
obj = 0
judge = 0
for i in range(n):
    words = input().split()
    for items in words:
        if items.startswith("###") and items.endswith("###"):
            if judge == 0:
                obj += 1
                judge = 1
            else:
                pass
        else:
            judge = 0

print(obj)