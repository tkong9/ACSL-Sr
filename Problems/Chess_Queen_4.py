import sys

sys.stdin = open('input.txt', 'r')


def calculate_safe_spots(positions, board_size):
    board = [[True for _ in range(board_size)] for _ in range(board_size)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for row in range(board_size):
        for col in range(board_size):
            for dx, dy in directions:
                for i in range(1, board_size):
                    new_row, new_col = row + dx * i, col + dy * i
                    if 0 <= new_row < board_size and 0 <= new_col < board_size:
                        board[new_row][new_col] = False

            for j in range(0, len(positions), 2):
                x, y = positions[j], positions[j + 1]
                if board[x][y]:
                    break
            else:
                return f'{row + 1} {col + 1}'
            board = [[True for _ in range(board_size)] for _ in range(board_size)]

    return 'NONE'


TC = int(input())
for t in range(1, TC + 1):
    positions = list(map(int, input().split()))[:-2]
    positions = [x - 1 for x in positions] # make it 0-based
    print(f'#{t} {calculate_safe_spots(positions, 8)}')
