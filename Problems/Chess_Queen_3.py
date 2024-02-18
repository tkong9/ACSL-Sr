def calculate_safe_spots(n, m, positions):
    board = [[True for _ in range(m)] for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
 
    for p in range(0, len(positions), 2):
        row, col = positions[p], positions[p + 1]
        for dx, dy in directions:
            for i in range(1, max(n, m)):
                new_row, new_col = row + dx * i, col + dy * i
                if 0 <= new_row < n and 0 <= new_col < m:
                    board[new_row][new_col] = False
 
    for p in range(0, len(positions), 2):
        row, col = positions[p], positions[p + 1]
        board[row][col] = False
 
    safe_spots = sum(sum(row) for row in board)
 
    return safe_spots
 
 
TC = int(input())
for t in range(1, TC + 1):
    data = list(map(int, input().split()))
    n, m, c, positions = data[0], data[1], data[2], data[3:]
    positions = [x - 1 for x in positions] # make it 0-based
    print(f'#{t} {calculate_safe_spots(n, m, positions)}')