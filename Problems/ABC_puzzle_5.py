import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')


# A helper function to get the row and column of a given index
def get_row_col(index, n):
    return index // n, index % n

# A helper function to get the index from row and col
def get_index(row, col, n):
    return row * n + col

# def is_valid(index, letter):
#     row, col = get_row_col(index, 4)
#     for i in range(6):
#         if grid[get_index(row, i, 4)] is None:
#             continue
#         # Check the row
#         if grid[get_index(row, i, 4)] == letter:
#             return False
#         # Check the column
#         if grid[get_index(i, col, 4)] == letter:
#             return False
#     return True

def could_place(letter, row, col):
    return not (letter in rows[row] or letter in cols[col])

def place(letter, row, col):
    rows[row][letter] += 1
    cols[col][letter] += 1
    grid[get_index(row, col, 4)] = letter

def remove(letter, row, col):
    del rows[row][letter]
    del cols[col][letter]
    grid[get_index(row, col, 4)] = None

def backtrack(index=0):
    if index == n * n:
        return True
    row, col = get_row_col(index, 4)
    # If this cell is already filled, move to the next cell
    if grid[index] is not None:
        return backtrack(index + 1)

    # Try to fill the cell with letters A, B, and C
    for letter in 'ABC':
        if could_place(letter, row, col):
            place(letter, row, col)
            if backtrack(index + 1):
                return True
            remove(letter, row, col)
    return False

def print_grid():
    for i in range(6):  # Assuming a 6x6 grid
        print(' '.join(str(cell) if cell is not None else '.' for cell in grid[i*6:(i+1)*6]))

def print_grid2():
    for i in range(4):  # Assuming a 4x4 grid
        for j in range(4):
            print(grid[get_index(i, j, 4)], end=' ')
        print()

def place_outside_letters_to_middle(letter, index):
    if 1 <= index <= 4: # downward
        index += 6
        while grid[index] == 'X':
            index += 6
        grid[index] = letter
    elif index in [6, 12, 18, 24]: # rightward
        index += 1
        while grid[index] == 'X':
            index += 1
        grid[index] = letter
    elif 31 <= index <= 34: # upward
        index -= 6
        while grid[index] == 'X':
            index -= 6
        grid[index] = letter
    elif index in [11, 17, 23, 29]: # leftward
        index -= 1
        while grid[index] == 'X':
            index -= 1
        grid[index] = letter

def return_middle_letters():
    middle_grid = []
    for i in range(36):
        row, col = get_row_col(i, 6)
        if 1 <= row <= 4 and 1 <= col <= 4:
            middle_grid.append(grid[i])
    return middle_grid


TC = int(input())
for T in range(1, TC + 1):
    n = 6
    input_data = input().split()
    blocked_cells = list(map(int, input_data[:4]))
    letters_num = int(input_data[4])
    letters_and_pos = input_data[5: - 1]
    letters_and_pos = [(letters_and_pos[i], int(letters_and_pos[i + 1])) for i in range(0, len(letters_and_pos), 2)]
    grid = [None] * 36
    # print(letters_and_pos)
    # Fill the grid with the blocked cells
    for i in blocked_cells:
        grid[i - 1] = 'X'
    # Fill the grid with the initial values
    for j in letters_and_pos:
        # Subtract 1 from the index because the input indexes start from 1
        index = j[1] - 1
        grid[index] = j[0]
    # Fill the grid with the letters that are outside the grid
    for letter, index in letters_and_pos:
        place_outside_letters_to_middle(letter, index - 1)

    n = 4
    rows = [defaultdict(int) for _ in range(n)]
    cols = [defaultdict(int) for _ in range(n)]

    grid = return_middle_letters()
    ans_position = int(input_data[-1])
    ans_row, ans_col = get_row_col(ans_position - 1, 6)
    ans_position = get_index(ans_row - 1, ans_col - 1, 4)

    # Initialize the rows and cols
    for i in range(n):
        for j in range(n):
            if grid[get_index(i, j, 4)] is not None:
                place(grid[get_index(i, j, 4)], i, j)

    # print_grid2()
    is_solved = backtrack()
    # print_grid2()
    if is_solved:
        # grid = ''.join(grid)
        # print(grid, end=' ')
        # print_grid2()
        print(f"#{T} {grid[ans_position]}")
    else:
        print(f"#{T} INVALID")


