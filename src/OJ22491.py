h = int(input()); h *= 2
m = int(input())
courses = [tuple(map(float, input().split())) for _ in range(m)]
progress = 0

h -= m*0.5
if h > 0:
    courses.sort(key = lambda x: -x[0]*x[1])
    i = 0
    while h > 0 and i < len(courses):
        h -= 5/courses[i][0]
        progress += 5*courses[i][1]
        i += 1

    if h < 0:
        progress -= (-h)*courses[i-1][0]*courses[i-1][1]

print(f'{progress:.1f}')