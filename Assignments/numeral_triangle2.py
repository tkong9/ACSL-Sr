'''
Numeral Triangle

Name: <your name>
'''
#
# Complete the 'sumOfLastRow' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING d
#  3. INTEGER r
#

def calcDigits(s):
    '''
    Calculate the sum of digits of a number.
    :param s:
    :return:
    '''
    string = hex(s)[2:] # convert to hexadecimal
    tot = 0
    for num in string:
        tot += int(num, 16)
    return tot


def sumOfLastRow(s, d, r):
    start_decimal = int(s, 16) # convert to decimal
    difference_decimal = int(d, 16) # convert to decimal
    row_length = r

    start_decimal += difference_decimal * (row_length - 1) * row_length // 2 # calculate the first number of the last row

    sum_digits = 0

    # calculate the sum of digits of the last row
    for _ in range(row_length):
        sum_digits += calcDigits(start_decimal)
        start_decimal += difference_decimal

    # calculate the sum of digits of the last row until it is a single digit
    sum_digits_hex = hex(sum_digits)[2:]
    while len(sum_digits_hex) > 1:
        sum_digits = calcDigits(sum_digits)
        sum_digits_hex = hex(sum_digits)[2:]
    return sum_digits_hex.capitalize()


if __name__ == '__main__':
    import sys
    '''
    Read test cases from stdin.
    To test your solution, make 'triangle_numeral_sample_data.txt'
    in the same directory as this file,
    paste the sample data from the question in that file,
    and run this code.
    (Sample data is also available below)
    '''
    sys.stdin = open('triangle_numeral_sample_data.txt', 'r')

    for i in range(10):
        data = input().split()

        s = data[0]
        d = data[1]
        r = int(data[2])

        result = sumOfLastRow(s, d, r)

        print('Test Case #{}: {}'.format(i + 1, result))

    '''
    Your output on console should be:
    Test Case #1: 5
    Test Case #2: C
    Test Case #3: A
    Test Case #4: F
    Test Case #5: 5
    Test Case #6: 5
    Test Case #7: F
    Test Case #8: 3
    Test Case #9: A
    Test Case #10: E
    '''


# Sample data:
# Copy and paste this in 'triangle_numeral_sample_data.txt' without the triple quotes
'''
A 9 5
ABC F 4
BAD 50 10
FED ABC 25
184 231 35
ABE CAB 40
31415 92653 60
DEAF BED 72
BAD DAD 100
704 1776 244
'''
