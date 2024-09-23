n = int(input())
n_bin = bin(n)[2:]

if n_bin == n_bin[::-1]:
    print("Yes")
else:
    print("No")
