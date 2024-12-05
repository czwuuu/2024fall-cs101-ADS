def put_queen(temp: list, answer: list, used = [False]*9) -> None:
    if len(temp) == 8:
        answer.append(temp[:])
        return
    else:
        for row in range(1, 9):
            if not used[row]:
                flag = True
                for col in range(1, len(temp)+1):
                    if abs(row - temp[col-1]) == abs(1 + len(temp) - col):
                        flag = False
                        break
                if flag:
                    used[row] = True
                    temp.append(row)
                    put_queen(temp, answer, used)
                    used[row] = False
                    temp.pop()
answer = []
put_queen([], answer)

test = int(input())
for _ in range(test):
    ans_l = answer[int(input())-1]
    print(''.join(list(map(str, ans_l))))

