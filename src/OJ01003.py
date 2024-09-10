results = []
while True:
    target = float(input())  # 读取输入
    if target == 0.00:  # 输入为0时退出循环
        break

    current_sum = 0
    cards = 0
    while current_sum < target:  # 累加计算，直到达到目标值
        cards += 1
        current_sum += 1 / (1 + cards)

    results.append(f"{cards} card(s)")  # 将结果保存到列表中

for result in results:
    print(result)  # 输出每个结果
