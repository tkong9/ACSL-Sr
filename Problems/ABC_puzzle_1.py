import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')


# A helper function to get the row and column of a given index
def get_row_col(index):
    return index // 3, index % 3

# A helper function to get the index from row and col
def get_index(row, col):
    return row * 3 + col

def is_valid(index, letter):
    row, col = get_row_col(index)
    for i in range(3):
        if grid[get_index(row, i)] is None:
            continue
        # Check the row
        if grid[get_index(row, i)] == letter:
            return False
        # Check the column
        if grid[get_index(i, col)] == letter:
            return False
    return True

def could_place(letter, row, col):
    return not (letter in rows[row] or letter in cols[col])

def place(letter, row, col):
    rows[row][letter] += 1
    cols[col][letter] += 1
    grid[get_index(row, col)] = letter

def remove(letter, row, col):
    del rows[row][letter]
    del cols[col][letter]
    grid[get_index(row, col)] = None

def backtrack(index=0):
    if index == 9:
        return True
    row, col = get_row_col(index)
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


TC = int(input())
for T in range(1, TC + 1):
    rows = [defaultdict(int) for _ in range(3)]
    cols = [defaultdict(int) for _ in range(3)]
    inputs = input().split()[1:]
    inputs = [(int(inputs[i]), inputs[i + 1]) for i in range(0, len(inputs), 2)]
    grid = [None] * 9

    # Fill the grid with the initial values
    for j in inputs:
        # Subtract 1 from the index because the input indexes start from 1
        index = j[0] - 1
        grid[index] = j[1]

    for index, letter in inputs:
        row, col = get_row_col(index - 1)
        place(letter, row, col)

    is_valid_board = True
    for i in range(3):
        for val in rows[i].values():
            if val > 1:
                is_valid_board = False
        for val in cols[i].values():
            if val > 1:
                is_valid_board = False
        if not is_valid_board: break

    is_solved = backtrack()
    if is_valid_board and is_solved:
        grid = ''.join(grid)
        print(f"#{T} {grid}")
    else:
        print(f"#{T} INVALID")
