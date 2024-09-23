n = int(input())
abre = []
for i in range(n):
    word = input()
    length = len(word)
    if length > 10:
        word = word[0]+f"{length-2}"+word[-1]
    abre.append(word)
for word in abre:
    print(word)