x = int(input())
while not(x == 1):
    if x % 2 != 0:
        x_new = x * 3 + 1
        print(f"{x}*3+1={x_new}")
        x = x_new
    else:
        x_new = int(x / 2)
        print(f"{x}/2={x_new}")
        x = x_new
