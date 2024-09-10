n = int(input())
crime_and_recruit = list(map(int, input().split()))
police = 0
untreated = 0
for i in range(n):
    if crime_and_recruit[i] != -1:
        if police < 0:
            police = 0
        police += crime_and_recruit[i]
    else:
        police -= 1
        if police < 0:
            untreated +=1
print(int(untreated))