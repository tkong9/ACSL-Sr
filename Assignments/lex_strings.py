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


# 1. This function will filter the alphanumeric characters from the string and sort them.
def filter_and_sort(s):
    alphanumeric_chars = ''.join(ch for ch in s if ch.isalnum())
    return sorted(alphanumeric_chars, reverse=True)


# 2. This function will take the sorted string and group the characters by their count.
def group_by_count(sorted_chars):
    char_count = Counter(sorted_chars)
    groups = defaultdict(list)
    for char, count in sorted(char_count.items(), key=lambda x: (-x[1], x[0])):
        groups[count].append(char)
    return groups


# 3. This function will take the groups and apply the alternating sort order.
def alternate_sort(groups):
    sorted_groups = []
    ascending_order = True
    for count, chars in sorted(groups.items(), reverse=True):
        chars = ''.join(chars)
        if not ascending_order:
            chars = chars[::-1]
        sorted_groups.append((count, chars))
        ascending_order = not ascending_order
    return sorted_groups


# 4. This function will take the sorted groups and format the result as required.
def format_result(sorted_groups):
    return ','.join(f"{count}{chars}" for count, chars in sorted_groups)


def rearrangedString(s):
    '''
    1. Extract alphanumeric characters: We'll start by extracting only alphanumeric characters from the input string.
    2. Create frequency groups: We'll group characters by their frequency, preserving the order of characters within each group.
    3. Sort and alternate groups: We'll sort the groups by frequency, and then apply the alternating order rule within each group.
    4. Concatenate and format: Finally, we'll concatenate the groups and format the result as required.
    '''
    # 1.
    sorted_chars = filter_and_sort(s)
    groups = group_by_count(sorted_chars)
    sorted_groups = alternate_sort(groups)
    result = format_result(sorted_groups)
    return result


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
