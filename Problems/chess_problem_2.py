import sys
sys.stdin = open('input.txt', 'r')

def calculate_score_difference(board):
    score_dic = {'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}
    w_sum, b_sum = 0, 0

    for row in board:
        for piece in row:
            if piece == '.':
                continue
            is_white = piece.isupper()
            score = score_dic[piece.upper()]
            if is_white:
                w_sum += score
            else:
                b_sum += score

    return w_sum - b_sum

TC = int(input())
for t in range(1, TC + 1):
    board = [input() for _ in range(8)]
    print(f'#{t} {calculate_score_difference(board)}')



# BREAK UNTIL 11:05











