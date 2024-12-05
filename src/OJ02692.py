n = int(input())
answer = []
coins = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5,
         'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
cmp = {'even':0, 'up':1, 'down':-1}
for _ in range(n):
    initialize = [1]*12
    test1 = input().split()
    test2 = input().split()
    test3 = input().split()
    found = False
    number = 0
    counterfeit = 'heavy'
    for i in range(12):
        test_condition = initialize[:]
        test_condition[i] += 1
        bool1 = test_condition[coins[test1[0][0]]]+test_condition[coins[test1[0][1]]]+test_condition[coins[test1[0][2]]]+test_condition[coins[test1[0][3]]]-test_condition[coins[test1[1][0]]]-test_condition[coins[test1[1][1]]]-test_condition[coins[test1[1][2]]]-test_condition[coins[test1[1][3]]] == cmp[test1[2]]
        bool2 = test_condition[coins[test2[0][0]]] + test_condition[coins[test2[0][1]]] + test_condition[coins[test2[0][2]]] + test_condition[coins[test2[0][3]]] - test_condition[coins[test2[1][0]]] - test_condition[coins[test2[1][1]]] - test_condition[coins[test2[1][2]]] - test_condition[coins[test2[1][3]]] == cmp[test2[2]]
        bool3 = test_condition[coins[test3[0][0]]] + test_condition[coins[test3[0][1]]] + test_condition[
            coins[test3[0][2]]] + test_condition[coins[test3[0][3]]] - test_condition[coins[test3[1][0]]] - \
                test_condition[coins[test3[1][1]]] - test_condition[coins[test3[1][2]]] - test_condition[
                    coins[test3[1][3]]] == cmp[test3[2]]
        if bool1 and bool2 and bool3:
            found = True
            number = i
            break
    if not found:
        counterfeit = 'light'
        for i in range(12):
            test_condition = initialize[:]
            test_condition[i] -= 1
            bool1 = test_condition[coins[test1[0][0]]] + test_condition[coins[test1[0][1]]] + test_condition[
                coins[test1[0][2]]] + test_condition[coins[test1[0][3]]] - test_condition[coins[test1[1][0]]] - \
                    test_condition[coins[test1[1][1]]] - test_condition[coins[test1[1][2]]] - test_condition[
                        coins[test1[1][3]]] == cmp[test1[2]]
            bool2 = test_condition[coins[test2[0][0]]] + test_condition[coins[test2[0][1]]] + test_condition[
                coins[test2[0][2]]] + test_condition[coins[test2[0][3]]] - test_condition[coins[test2[1][0]]] - \
                    test_condition[coins[test2[1][1]]] - test_condition[coins[test2[1][2]]] - test_condition[
                        coins[test2[1][3]]] == cmp[test2[2]]
            bool3 = test_condition[coins[test3[0][0]]] + test_condition[coins[test3[0][1]]] + test_condition[
                coins[test3[0][2]]] + test_condition[coins[test3[0][3]]] - test_condition[coins[test3[1][0]]] - \
                    test_condition[coins[test3[1][1]]] - test_condition[coins[test3[1][2]]] - test_condition[
                        coins[test3[1][3]]] == cmp[test3[2]]
            if bool1 and bool2 and bool3:
                found = True
                number = i
                break
    answer.append(chr(65+number)+' is the counterfeit coin and it is '+counterfeit+'.')
for ans in answer:
    print(ans)