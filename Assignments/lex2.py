'''
Lex Strings

Name: <your name>
'''
from collections import Counter, defaultdict

#
# Complete the 'rearrangedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#
from operator import itemgetter


def form_blocks(saved_chars):
    key = None
    curr_block = None
    blocks = []
    for item_num in range(len(saved_chars)):
        if saved_chars[item_num] != key:
            key = saved_chars[item_num]
            # print("new key:", key)
            curr_block = saved_chars[item_num]
            blocks.append(curr_block)
        else:
            blocks[-1] += key
            # print("added on.")
            # print("updated curr_block.len:", len(curr_block))

    # print("done with process")

    # for item in blocks:
    #     print(item)

    return blocks


def compress(blocks):
    overall_list = []
    while len(blocks) != 0:
        curr_len_list = []
        item = blocks[0]
        curr_len = len(item)
        curr_len_list.append(str(curr_len))
        dummy_blocks = blocks.copy()

        while len(dummy_blocks) != 0:
            # print("\nlen(dummy_blocks):", len(dummy_blocks))
            # print("dummy_blocks:", dummy_blocks)
            curr_item = dummy_blocks[0]
            # print("curr_item:", curr_item)
            if len(curr_item) == curr_len:
                curr_len_list.append(curr_item[0])
                blocks.remove(curr_item)
            dummy_blocks.pop(0)
        overall_list.append(curr_len_list)
        # print("big cycle done. blocks:", blocks)
        # print("overall_list:", overall_list)
        # if len(blocks) != 0:
        # blocks.pop(0)

    return overall_list


def rearrangedString(s):
    saved_chars = []
    for char_num in range(len(s)):
        if s[char_num].isalnum():
            # print(s[char_num], "is saved")
            saved_chars.append(s[char_num])
    # print(saved_chars)
    saved_chars = sorted(saved_chars)

    blocks = form_blocks(saved_chars)
    # print(blocks)
    overall_list = sorted(compress(blocks), key=itemgetter(0), reverse=True)

    # print(overall_list)

    final_list = []

    for block in overall_list:
        curr_str = block[0]
        block.pop(0)
        block_num = overall_list.index(block) + 1
        if block_num % 2 == 1:
            block = sorted(block)
            final_list.append(curr_str + "".join(block))
        elif block_num % 2 == 0:
            block = sorted(block, reverse=True)
            final_list.append(curr_str + "".join(block))

    # print(final_list)
    return ",".join(final_list)


if __name__ == '__main__':
    import sys

    sys.stdin = open('lex_strings_sample_data.txt', 'r')
    for tc in range(10):
        s = input()
        result = rearrangedString(s)
        print('Test Case #{}: {}'.format(tc + 1, result))

'''
Your output on console should be:
Test Case #1: 6in,4ts,3aegr,2o,1ESTfhlmpx
Test Case #2: 5a,4se,3r,2tonkihc,1ACFHLRSdflmuwy
Test Case #3: 2135ei,1tsrohgfdaTPI9642
Test Case #4: 7es,4lh,2a,1ytrobS
Test Case #5: 8a,5n,4gu,3rlic,2CPSdehmosty,1vbVRJIBA
Test Case #6: 7ae,6ni,5t,4rhd,3gl,2vsoc,119CDIOVbmpuwy
Test Case #7: 9e,5nica,4or,3th,202CTsu,1vpmlfdSA
Test Case #8: 53,472,345689deo,2trni1,1IPTafghsu
Test Case #9: 14e,13p,7i,6r,5cdk,4P,2alost,1ywnmfH
Test Case #10: 8o,7e,5hn,3wtsrda,2ikp,1ylfbT10
'''
