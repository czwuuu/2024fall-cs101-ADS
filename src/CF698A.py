def count_rest(seq, counter = 0):
    if len(seq) > 1:
        sub_seq = seq[:-1]
        last_ele = seq[-1]
        if last_ele == 0:
            counter = count_rest(sub_seq, counter) + 1
        elif last_ele == 3:
            counter = count_rest(sub_seq, counter)
        else:
            if last_ele == sub_seq[-1]:
                sub_seq[-1] = 0
                counter = count_rest(sub_seq, counter)
            else:
                if sub_seq[-1] == 3:
                    sub_seq[-1] = 2 if last_ele == 1 else 1
                counter = count_rest(sub_seq, counter)
        return counter
    else:
        return 0

n = int(input())
arr = list(map(int, input().split()))
print(count_rest([3]+arr))