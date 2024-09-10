n, k = map(int, input().split())
a = list(map(int, input().split()))
if a[0] == 0 :
    print(0)
elif a[k-1] == 0 :
    result = k
    while a[result-1] == 0 :
        result -= 1
    print(result)
elif a[k-1] != a[n-1] :
    result = k
    while a[result] == a[result -1] :
        result += 1
    print(result)
else :
    print(n)