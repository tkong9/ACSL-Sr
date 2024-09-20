'''
Lex Strings

Name: <your name>
'''
#
# Complete the 'rearrangedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#
import re

def rearrangedString(s):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)

    sorted_string = ''.join(sorted(cleaned_string))

    char_count = {}
    for char in sorted_string:
        char_count[char] = char_count.get(char, 0) + 1

    sorted_counts = sorted(char_count.items(), key=lambda x: x[1])

    grouped_blocks = {}
    for char, count in sorted_counts:
        if count not in grouped_blocks:
            grouped_blocks[count] = []
        grouped_blocks[count].append(char)

    sorted_blocks = sorted(grouped_blocks.items(), key=lambda x: (-x[0], ''.join(sorted(x[1]))))

    compressed_format = ''
    for size, chars in sorted_blocks:
    	compressed_format+=str(size)
    	for ch in chars:
    		compressed_format+= ch
    	compressed_format += ", "

    return compressed_format



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