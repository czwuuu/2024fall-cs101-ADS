n = int(input())
l = input().split()

def min_link(li):
    link = sorted(li[:])
    swapped = True
    for i in range(len(link)-1):
        if swapped:
            swapped = False
            for j in range(len(link)-1-i):
                if link[j]+link[j+1] > link[j+1]+link[j]:
                    link[j], link[j+1] = link[j+1], link[j]
                    swapped = True
        else:
            break
    return link

print(''.join(reversed(min_link(l))), ''.join(min_link(l)))