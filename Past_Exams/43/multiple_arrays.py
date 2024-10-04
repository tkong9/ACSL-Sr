# import sys
#
# sys.stdin = open('multiple_arrays.txt', 'r')
#
# def solve():
#     row, col = map(int, input().split())
#
#     multi_arrays = {
#         1: [],
#         2: [],
#         3: []
#     }
#
#     for arr_num in range(1, 4):
#         row_major = list(map(int, input().split()))
#         for i in range(0, row * col, col):
#             nth_row = row_major[i: i + col]
#             multi_arrays[arr_num].append(nth_row)
#
#     current_pos = (0, 0)
#     global_path = []
#     while current_pos[0] != row - 1 and current_pos[1] != col - 1:
#         current_row, current_col = current_pos
#         current_path = []
#         pos_val_pair = {
#             1: dict(),
#             2: dict(),
#             3: dict()
#         }
#
#         for i in range(1, 4):
#             nth_array = multi_arrays[i]
#             current_path.append(nth_array[current_row][current_col])
#
#             right_val = nth_array[current_row][current_col + 1]  # check right
#             down_val = nth_array[current_row + 1][current_col]  # check down
#
#             pos_val_pair[i][(current_row, current_col + 1)] = right_val
#             pos_val_pair[i][(current_row + 1, current_col)] = down_val
#
#         global_path.append(current_path)
#         values = []
#         for v in pos_val_pair.values():
#             values.extend(v.values())
#
#         max_val = max(values)
#
#         if values.count(max_val) > 1:
#             current_pos = (current_row + 1, current_col + 1)
#             continue
#         for k, v in pos_val_pair.items():
#             if max_val in v.values():
#                 for k1, v1 in v.items():
#                     if v1 == max_val:
#                         current_pos = k1
#                         break
#                 break
#
#     current_path = []
#     for i in range(1, 4):
#         nth_array = multi_arrays[i]
#         current_path.append(nth_array[current_pos[0]][current_pos[1]])
#     global_path.append(current_path)
#
#     ans = 0
#     for v in global_path:
#         ans += min(v)
#     print(ans)
#
# for tc in range(8):
#     solve()

import sys

sys.stdin = open('multiple_arrays.txt', 'r')

def solve():
    row, col = map(int, input().split())

    multi_arrays = []

    # Storing arrays as a list of lists (0-indexed for simplicity)
    for _ in range(3):
        row_major = list(map(int, input().split()))
        multi_arrays.append([row_major[i:i + col] for i in range(0, row * col, col)])

    current_pos = (0, 0)
    global_path = [] # Store the path of the values at each cell

    while current_pos[0] != row - 1 and current_pos[1] != col - 1:
        current_row, current_col = current_pos

        values = [] # Store the values of the right and down cells
        candidates = [] # Store the positions and values of the right and down cells

        # Check right and down for each array and collect values
        for arr in multi_arrays:
            right_val = arr[current_row][current_col + 1] if current_col + 1 < col else float('-inf')
            down_val = arr[current_row + 1][current_col] if current_row + 1 < row else float('-inf')

            values.extend([right_val, down_val])
            candidates.append(((current_row, current_col + 1), right_val))
            candidates.append(((current_row + 1, current_col), down_val))

        global_path.append([arr[current_row][current_col] for arr in multi_arrays])

        max_val = max(values)

        # If the max value appears more than once, move diagonally
        if values.count(max_val) > 1:
            current_pos = (current_row + 1, current_col + 1)
        else:
            # Otherwise, move to the position with the maximum value
            for pos, val in candidates:
                if val == max_val:
                    current_pos = pos
                    break
        print(candidates)
    # Append the final position to the path
    global_path.append([arr[current_pos[0]][current_pos[1]] for arr in multi_arrays])
    # Calculate the result by summing the minimum value at each visited cell
    ans = sum(min(values) for values in global_path)
    print(ans)


for tc in range(1):
    solve()
