N = int(input())
answer = []
epsilon = 1e-6
for b in range(2, int(N/(3**(1/3)))+1):
    for c in range(b, int(N/(2**(1/3)))+1):
        for d in range(c, N+1):
            if N**3 < b**3+c**3+d**3:
                break
            a = (b**3+c**3+d**3)**(1/3)
            if abs(a-round(a)) <= epsilon:
                a = round(a)
                answer.append((a, b, c, d))
answer.sort()
for ans in answer:
    print(f"Cube = {ans[0]}, Triple = ({ans[1]},{ans[2]},{ans[3]})")
