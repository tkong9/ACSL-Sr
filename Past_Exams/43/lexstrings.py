# import sys, heapq
#
# sys.stdin = open('lexstrings.txt', 'r')
#
#
# def extract_same_char_block(s, idx):
#     while idx < len(s) - 1 and s[idx + 1] == s[idx]:
#         idx += 1
#     return idx
#
#
# if __name__ == '__main__':
#     for tc in range(10):
#         given_str, max_len = input().split()
#         max_len = int(max_len)
#         left_idx = 0
#         priority_heap = []
#         while left_idx < len(given_str):
#             right_idx = extract_same_char_block(given_str, left_idx)
#             block = given_str[left_idx: right_idx + 1]
#             heapq.heappush(priority_heap, (-len(block), block))
#             left_idx = right_idx + 1
#
#         blocks = []
#         while priority_heap:
#             _, block = heapq.heappop(priority_heap)
#             blocks.append(block)
#
#         # print(blocks)
#
#         combined_blocks = "".join(blocks)
#
#         # print(combined_blocks)
#         final_answer = combined_blocks[0]
#         same_letter_cnt = 1
#
#         for i in range(1, len(combined_blocks)):
#             if combined_blocks[i] == combined_blocks[i - 1]:
#                 same_letter_cnt += 1
#             else:
#                 same_letter_cnt = 1
#
#             if same_letter_cnt <= max_len:
#                 final_answer += combined_blocks[i]
#             else:
#                 continue
#         print(f"{tc + 1}. {final_answer}")
#


import sys, heapq

# Open the file for reading input
sys.stdin = open('lexstrings.txt', 'r')


def extract_same_char_block(s, idx):
    """
    Returns the last index of a block of the same consecutive character starting from index `idx`.
    """
    while idx < len(s) - 1 and s[idx + 1] == s[idx]:
        idx += 1
    return idx


if __name__ == '__main__':
    for tc in range(10):  # Adjust number of test cases as needed
        given_str, max_len = input().split()
        max_len = int(max_len)

        # Initialize variables
        left_idx = 0
        priority_heap = []

        # Extract blocks of consecutive same characters
        while left_idx < len(given_str):
            right_idx = extract_same_char_block(given_str, left_idx)
            block = given_str[left_idx:right_idx + 1]
            heapq.heappush(priority_heap, (-len(block), block))  # Push block with negative length for max-heap behavior
            left_idx = right_idx + 1

        # Retrieve blocks in order from heap
        blocks = []
        while priority_heap:
            _, block = heapq.heappop(priority_heap)
            blocks.append(block)

        # Combine all blocks into a single string
        combined_blocks = "".join(blocks)

        # Build final answer with the given max length constraint
        final_answer = combined_blocks[0]  # Start with the first character
        same_letter_cnt = 1

        for i in range(1, len(combined_blocks)):
            if combined_blocks[i] == combined_blocks[i - 1]:
                same_letter_cnt += 1
            else:
                same_letter_cnt = 1

            if same_letter_cnt <= max_len:
                final_answer += combined_blocks[i]

        # Output the result for the current test case
        print(f"{tc + 1}. {final_answer}")