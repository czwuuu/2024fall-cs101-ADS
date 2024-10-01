from math import ceil
ans = []
while True:
    packages = list(map(int, input().split()))
    if packages == [0, 0, 0, 0, 0, 0]:
        break
    else:
        least_pac = 0
        least_pac += packages[-1]+packages[-2]
        packages[0] = max(packages[0]-11*packages[-2], 0)

        least_pac += packages[3]
        diff1 = 5*packages[3]-packages[1]
        packages[1] = max(packages[1]-5*packages[3], 0)
        if packages[1] == 0:
            restroom = (diff1)*4
            if packages[0] > 0:
                packages[0] = max(packages[0]-restroom, 0)

        pac_for_3 = ceil(packages[2]/4)
        least_pac += pac_for_3
        pac_3_restroom = pac_for_3*4-packages[2]

        if pac_3_restroom == 1:
            orig_packages1 = packages[1]
            packages[1] = max(packages[1]-1, 0)
            diff = orig_packages1-packages[1]
            packages[0] = max(packages[0] - (9 - diff*4), 0)
        elif pac_3_restroom == 2:
            orig_packages1 = packages[1]
            packages[1] = max(packages[1]-3, 0)
            diff = orig_packages1 - packages[1]
            packages[0] = max(packages[0] - (18 - diff*4), 0)
        elif pac_3_restroom == 3:
            orig_packages1 = packages[1]
            packages[1] = max(packages[1]-5, 0)
            diff = orig_packages1 - packages[1]
            packages[0] = max(packages[0] - (27 - diff*4), 0)

        pac_for_2 = ceil(packages[1]/9)
        least_pac += pac_for_2
        pac_2_restroom = (pac_for_2*9-packages[1])*4
        if packages[0] > pac_2_restroom:
            packages[0] -= pac_2_restroom
        else:
            packages[0] = 0

        least_pac += ceil(packages[0]/36)
    ans.append(least_pac)

for item in ans:
    print(item)