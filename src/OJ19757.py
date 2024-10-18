# answer = []
#
# while True:
#     R, n = map(int, input().split())
#     if R == -1 and n == -1:
#         break
#     else:
#         stones = 0
#         x = list(map(int, input().split()))
#         x.sort()
#         covered = -1
#         i = 0
#         while i < n:
#             if covered == n-1:
#                 break
#             if x[i]-x[covered+1] <= R:
#                 i += 1
#             else:
#                 stones += 1
#                 i -= 1
#                 covered = i
#                 while True:
#                     if x[covered] - x[i] <= R:
#                         if covered == n-1:
#                             break
#                         covered += 1
#                     else:
#                         covered -= 1
#                         i = covered + 1
#                         break
#         if i == n:
#             stones += 1
#         answer.append(stones)
#
# for ans in answer:
#     print(ans)

'''减少不必要的回溯'''

answer = []

while True:
    R, n = map(int, input().split())
    if R == -1 and n == -1:
        break
    else:
        stones = 0
        x = list(map(int, input().split()))
        x.sort()
        i = 0

        while i < n:
            # 找到离当前位置最远的可以覆盖的位置
            start = x[i]
            i += 1
            while i < n and x[i] <= start + R:
                i += 1

            # 放置石头
            stones += 1
            marker = x[i - 1]

            # 找到最后一个可以被当前石头覆盖的点
            while i < n and x[i] <= marker + R:
                i += 1

        answer.append(stones)

for ans in answer:
    print(ans)
