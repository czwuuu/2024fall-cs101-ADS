
def update(board, n, m):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    new_board = [[0]*m for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            count = -board[i][j]
            for x in dx:
                for y in dy:
                    count += board[i+x][j+y]
            if count < 2 or count > 3:
                new_board[i-1][j-1] = 0
            elif count == 3:
                new_board[i-1][j-1] = 1
            elif count == 2:
                new_board[i-1][j-1] = board[i][j]
    return new_board

def print_unpacked(board):
    for row in board:
        print(*row)

def main():
    n, m = map(int, input().split())

    board = [[0 for _ in range(m+2)]]
    for y in range(n):
        board.append([0]+[int(x) for x in input().split()]+[0])
    board.append([0 for _ in range(m+2)])

    new_board = update(board, n, m)
    print_unpacked(new_board)

if __name__ == "__main__":
    main()