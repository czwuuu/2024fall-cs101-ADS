n = int(input())
dates = []*n
for i in range(n):
    dates.append(input())
w_s = [0]*n

for i in range(n):
    c = int(dates[i][0:2])
    y = int(dates[i][2:4])
    m = int(dates[i][4:6])
    if m == 1 or m == 2:
        m += 12
        if y > 0:
            y -= 1
        else:
            c -= 1
            y = 99
    d = int(dates[i][6:8])
    w_s[i] = (y + int(y/4) + int(c/4) -2 * c
              + int(2.6 * (m + 1)) + d - 1) % 7


dic = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",
       5:"Friday", 6:"Saturday", 0:"Sunday"}

for i in range(n):
    print(dic[w_s[i]])