def check_cyclic(string):
    flag = True
    orig = int(string)
    cycle = [string]
    for i in range(1, len(string)):
        cycle.append((string[i:]+string[:i]))
    for i in range(2, len(string)+1):
        new_num = str(i*orig).rjust(len(string), '0')
        if new_num not in cycle:
            flag = False
            break
    return flag

datas = []
while True:
    try:
        datas.append(input())
    except EOFError:
        for data in datas:
            print(data + ' is cyclic' if check_cyclic(data)
                  else data + ' is not cyclic')
        break