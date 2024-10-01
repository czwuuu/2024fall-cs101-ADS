n = int(input())
laptops = [tuple(map(int, input().split())) for _ in range(n)]
laptops.sort()
quality = float("-inf")
winner = "Dima"
for laptop in laptops:
    if laptop[1] > quality:
        quality = laptop[1]
    else:
        winner = "Alex"
if winner == "Alex":
    print("Happy Alex")
else:
    print("Poor Alex")