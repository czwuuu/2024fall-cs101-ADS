M, N = map(int, input().split())
result = 0
if M == 1 :
    result = N//2
elif M >= 2 :
    if M%2 == 0:
        result = M*N/2
    else :
        result = (M-1)*N/2 + N//2
print(int(result))