import sys
import heapq

sys.stdin = open('input.txt', 'r')


def num_to_position(num):
    """Convert a tile number to its (row, column) position on the board."""
    return ((num - 1) // 7, (num - 1) % 7)


def position_to_num(row, col):
    """Convert a (row, column) position back to the tile number."""
    return (row * 7 + col) + 1


def get_longest_path_from_input():
    """Determine the longest path based on the current and blocked positions."""
    positions = list(map(num_to_position, map(int, input().split()[:-1])))
    current_position = positions[1]
    blocked_positions = set(positions[:1] + positions[2:])
    longest_path = []
    largest_path_sum = 0
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # down-right, down-left, up-right, up-left
    pq = []

    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)] + diagonal_directions: # down, right, up, left
        path_in_direction = []
        path_sum = 0

        for steps in range(1, 7):
            next_row = current_position[0] + steps * direction[0]
            next_col = current_position[1] + steps * direction[1]
            next_position = (next_row, next_col)

            if (next_position in blocked_positions or
                    not (0 <= next_row < 7) or
                    not (0 <= next_col < 7)):
                break

            path_sum += position_to_num(next_row, next_col)
            path_in_direction.append(next_position)

        heapq.heappush(pq, (-len(path_in_direction), -path_sum, path_in_direction))

        # if len(path_in_direction) > len(longest_path):
        #     longest_path = path_in_direction
        #     largest_path_sum = path_sum
        # elif len(path_in_direction) == len(longest_path) and path_sum > largest_path_sum:
        #     longest_path = path_in_direction
        #     largest_path_sum = path_sum
    # print(pq)
    print(pq)
    return heapq.heappop(pq)[-1]


TC = int(input())

for i in range(1, TC + 1):
    is_diagonal = False
    longest_path_positions = get_longest_path_from_input()
    if longest_path_positions:
        result = "->".join(str(position_to_num(row, col)) for row, col in longest_path_positions)
    else:
        result = "NONE"
    print(f'#{i} {result}')
