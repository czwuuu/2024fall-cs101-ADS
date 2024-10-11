def rome_to_int(rome):
    ret = 0
    i = 0
    while i < len(rome):
        if rome[i] == 'I':
            if i != len(rome)-1:
                if rome[i+1] == "V":
                    ret += 4
                    i += 2
                elif rome[i+1] == "X":
                    ret += 9
                    i += 2
                else:
                    ret += 1
                    i += 1
            else:
                ret += 1
                i += 1
        elif rome[i] == "V":
            ret += 5
            i += 1
        elif rome[i] == "X":
            if i != len(rome) - 1:
                if rome[i+1] == "L":
                    ret += 40
                    i += 2
                elif rome[i+1] == "C":
                    ret += 90
                    i += 2
                else:
                    ret += 10
                    i += 1
            else:
                ret += 10
                i += 1
        elif rome[i] == "L":
            ret += 50
            i += 1
        elif rome[i] == "C":
            if i != len(rome) - 1:
                if rome[i+1] == "D":
                    ret += 400
                    i += 2
                elif rome[i+1] == "M":
                    ret += 900
                    i += 2
                else:
                    ret += 100
                    i += 1
            else:
                ret += 100
                i += 1
        elif rome[i] == 'D':
            ret += 500
            i += 1
        else:
            ret += 1000
            i += 1
    return ret




def int_to_rome(n):
    ret = ''
    n = int(n)

    ret = ret + 'M'*(n//1000)
    n = n % 1000

    if len(str(n)) == 3:
        if str(n)[0] == '9':
            ret += 'CM'
            n = int(str(n)[1:])
        elif str(n)[0] == '4':
            ret += 'CD'
            n = int(str(n)[1:])
        elif str(n)[0] >= '5':
            ret += 'D'
            n -= 500

    if len(str(n)) == 3:
        ret += 'C'*int(str(n)[0])
        n = int(str(n)[1:])

    if len(str(n)) == 2:
        if str(n)[0] == '9':
            ret += 'XC'
            n = int(str(n)[1:])
        elif str(n)[0] == '4':
            ret += 'XL'
            n = int(str(n)[1:])
        elif str(n)[0] >= '5':
            ret += 'L'
            n -= 50

    if len(str(n)) == 2:
        ret += 'X'*int(str(n)[0])
        n = int(str(n)[1:])

    if len(str(n)) == 1 and n > 0:
        if n == 9:
            ret += 'IX'
            n = 0
        elif n == 4:
            ret += 'IV'
            n = 0
        elif n >= 5:
            ret += 'V'
            n -= 5

    if len(str(n)) == 1 and n > 0:
        ret += 'I'*n
        n = 0

    return ret




number = input()
if '0' <= number[0] <= '9':
    print(int_to_rome(number))
else:
    print(rome_to_int(number))