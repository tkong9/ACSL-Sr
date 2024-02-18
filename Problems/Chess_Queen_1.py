import sys

sys.stdin = open('input.txt', 'r')

def calculate_safe_spots(position, n, board_size):
    board = [[True for _ in range(board_size)] for _ in range(board_size)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    row, col = position
    for dx, dy in directions:
        for i in range(1, n + 1):
            new_row, new_col = row + dx * i, col + dy * i
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                board[new_row][new_col] = False

    board[row][col] = False
    safe_spots = sum(sum(row) for row in board)

    return safe_spots

TC = int(input())
for i in range(1, TC + 1):
    s_row, s_col, n = list(map(int, input().split()))
    s_row, s_col = s_row - 1, s_col - 1
    print(f'#{i} {calculate_safe_spots((s_row, s_col), n, 5)}')
