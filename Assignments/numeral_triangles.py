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

def sumOfLastRow(s, d, r):
    # Write your code here


if __name__ == '__main__':
    '''
    Read test cases from stdin.
    To test your solution, make 'triangle_numeral_sample_data.txt'
    in the same directory as this file,
    paste the sample data from the question in that file,
    and run this code.
    (Sample data is also available below)
    '''
    import sys
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
