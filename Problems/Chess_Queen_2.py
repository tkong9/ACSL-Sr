import sys

sys.stdin = open('input.txt', 'r')

def calculate_safe_spots(position, n, board_size):
    board = [[True for _ in range(board_size)] for _ in range(board_size)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    row1, col1, row2, col2 = position
    for dx, dy in directions:
        for i in range(1, n + 1):
            new_row1, new_col1, new_row2, new_col2 = row1 + dx * i, col1 + dy * i, row2 + dx * i, col2 + dy * i
            if 0 <= new_row1 < board_size and 0 <= new_col1 < board_size:
                board[new_row1][new_col1] = False
            if 0 <= new_row2 < board_size and 0 <= new_col2 < board_size:
                board[new_row2][new_col2] = False

    board[row1][col1] = False
    board[row2][col2] = False
    safe_spots = sum(sum(row) for row in board)

    return safe_spots

TC = int(input())
for i in range(1, TC + 1):
    s1_row, s1_col, s2_row, s2_col, n = list(map(int, input().split()))
    s1_row, s1_col, s2_row, s2_col = s1_row - 1, s1_col - 1, s2_row - 1, s2_col - 1
    print(f'#{i} {calculate_safe_spots((s1_row, s1_col, s2_row, s2_col), n, 8)}')
