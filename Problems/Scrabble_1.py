def get_raw_score(letter):
    letter_scores = {'A': 1, 'E': 1, 'D': 2, 'R': 2, 'B': 3, 'M': 3, 'V': 4, 'Y': 4, 'J': 8, 'X': 8}
    return letter_scores.get(letter, 0)

def calculate_scrabble_score(word, positions):
    total_scores = []
    for start in positions:
        triple_word = False
        double_word = False
        total_score = 0
        for j, letter in enumerate(word):
            letter_multiplier = False
            score = get_raw_score(letter)
            n = start + j
     
            if n % 3 == 0 and ((n // 3) % 2 == 1):
                score *= 2
                letter_multiplier = True
            elif n % 5 == 0:
                score *= 3
                letter_multiplier = True
     
            total_score += score
     
            if not letter_multiplier:
                if n % 8 == 0: 
                    triple_word = True
                elif n % 7 == 0: 
                    double_word = True
     
        if triple_word:
            total_score *= 3
        elif double_word:
            total_score *= 2
        total_scores.append(total_score)
 
    return total_scores


TC = int(input())
for t in range(1, TC + 1):
    word = input().split()
    start_positions = [int(input()) for _ in range(5)]
    answers = calculate_scrabble_score(word, start_positions)
    for i in range(5):
        print(f'#{t}.{i + 1} {answers[i]}')