# ans = []
#
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     else:
#         #生成酒店列表
#         hotels = [tuple(map(int, input().split())) for _ in range(N)]
#         hotels.sort()
#
#         i = 1
#         while i < len(hotels):
#             if hotels[i][0] == hotels[i-1][0] or hotels[i][1] >= hotels[i-1][1]:
#                 del hotels[i]
#             else:
#                 i += 1
#         ans.append(len(hotels))
#
# for item in ans:
#     print(item)


ans = []

while True:
    N = int(input())
    if N == 0:
        break

    # Read and sort the hotel data
    hotels = [tuple(map(int, input().split())) for _ in range(N)]
    hotels.sort()

    # Initialize variables
    selected_hotels = 0
    max_cost = float('inf')

    # Process each hotel
    for hotel in hotels:
        if hotel[1] < max_cost:
            selected_hotels += 1
            max_cost = hotel[1]

    ans.append(selected_hotels)

# Output the result
for item in ans:
    print(item)


'''log: del操作消耗大量时间，复杂度为N^2.在gpt提示下解决'''