# n, m, k = map(int, input().split())
# moves = [tuple(map(int, input().split())) for i in range(1, k+1)]
# answer = 0
# for i in range(k):
#     set_moves = set(moves[:i+1])
#     move = moves[i]
#     if ((move[0]+1, move[1]) in set_moves) and ((move[0], move[1]+1) in set_moves) and ((move[0]+1, move[1]+1) in set_moves):
#         answer = int(i+1)
#         break
#     elif ((move[0]-1, move[1]) in set_moves) and ((move[0], move[1]-1) in set_moves) and ((move[0]-1, move[1]-1) in set_moves):
#         answer = int(i+1)
#         break
#     elif ((move[0]-1, move[1]) in set_moves) and ((move[0], move[1]+1) in set_moves) and ((move[0]-1, move[1]+1) in set_moves):
#         answer = int(i+1)
#         break
#     elif ((move[0]+1, move[1]) in set_moves) and ((move[0], move[1]-1) in set_moves) and ((move[0]+1, move[1]-1) in set_moves):
#         answer = int(i+1)
#         break
# print(answer)

n, m, k = map(int, input().split())
moves = [tuple(map(int, input().split())) for _ in range(k)]
occupied = set()
answer = 0

for i, (x, y) in enumerate(moves):
    occupied.add((x, y))
    # Check if this move forms the bottom-right corner of a 2x2 square
    if (x-1, y) in occupied and (x, y-1) in occupied and (x-1, y-1) in occupied:
        answer = i + 1
        break
    # Check if this move forms the top-right corner of a 2x2 square
    if (x+1, y) in occupied and (x+1, y-1) in occupied and (x, y-1) in occupied:
        answer = i + 1
        break
    # Check if this move forms the bottom-left corner of a 2x2 square
    if (x, y+1) in occupied and (x-1, y+1) in occupied and (x-1, y) in occupied:
        answer = i + 1
        break
    # Check if this move forms the top-left corner of a 2x2 square
    if (x+1, y+1) in occupied and (x+1, y) in occupied and (x, y+1) in occupied:
        answer = i + 1
        break

print(answer)

'''本题由ChatGPT解决'''
'''优化点：每次构建set需要的时间较长，不如从一开始就构建一个occupied。复杂度从N^2到N'''
'''空间换时间'''
