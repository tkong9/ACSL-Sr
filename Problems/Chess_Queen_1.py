import sys

sys.stdin = open('input.txt', 'r')

def calculate_safe_spots(position, n, board_size):
    # Initialize the board with all spots safe
    board = [[True for _ in range(board_size)] for _ in range(board_size)]
    # Define directions a queen can move: vertical, horizontal, diagonal
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Mark the moves of the queen as unsafe
    row, col = position
    for dx, dy in directions:
        for i in range(1, n + 1):
            new_row, new_col = row + dx * i, col + dy * i # Move in the direction
            if 0 <= new_row < board_size and 0 <= new_col < board_size: # Check if the move is within the board
                board[new_row][new_col] = False # Mark the spot as unsafe

    # Exclude the queen's own position
    board[row][col] = False
    # Count the safe spots
    safe_spots = sum(sum(row) for row in board)

    return safe_spots

TC = int(input())
for i in range(1, TC + 1):
    s_row, s_col, n = list(map(int, input().split()))
    s_row, s_col = s_row - 1, s_col - 1
    print(f'#{i} {calculate_safe_spots((s_row, s_col), n, 5)}')
