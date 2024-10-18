def coding(mes, key):
    new_mes = [0]*len(key)
    for i in range(len(key)):
        new_mes[key[i]-1] = mes[i]
    return new_mes
def find_cycle(key):
    visited = [False]*len(key)
    cycles = []
    for start in range(len(key)):
        if not visited[start]:
            current = start
            cycle = []
            while not visited[current]:
                visited[current] = True
                cycle.append(current+1)
                current = key[current]-1
            cycles.append(cycle)
    return cycles

from collections import deque

answer = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        sec_key = list(map(int, input().split()))
        this_cycle = find_cycle(sec_key)
        while True:
            line = input()
            if line == '0':
                break
            else:
                k, message = line.split(" ", 1)
                k = int(k)
                message = list(message)
                message.extend([' ']*(n-len(message)))
                new_message = message[:]
                for cycle in this_cycle:
                    cyc = deque(cycle)
                    cyc.rotate(k%len(cycle))
                    for i in range(len(cyc)):
                        new_message[cycle[i]-1] = message[cyc[i]-1]
                answer.append(''.join(new_message))
        answer.append('')
for ans in answer:
    print(ans)

