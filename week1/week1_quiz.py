"""
Week 1 quiz
"""

"""
Q1. First Factorial

Recursion Challenge
Have the function RecursionChallenge(num) take the num parameter being passed and return the
factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
For the test cases, the range will be between 1 and 18 and the input will always be an integer.
"""
def RecursionChallenge(num):
    # Todo: your code goes here
    pass

"""
Q2. Power Sets

Set Challenge
Have the function SetChallenge(arr) take the array of integers stored in arr, and return the length
of the power set (the number of all possible sets) that can be generated.
For example: if arr is [1, 2, 3], then the following sets form the power set:
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
Hence with the given example, the output will be 8.
"""
def SetChallenge(arr):
    # Todo: your code goes here
    pass


"""
Q3. Closest Enemy

Array Challenge
Have the function ArrayChallenge(arr) take the array of numbers stored in arr and from the position
in the array where a 1 is, return the number of spaces either left or right you must move to reach
an enemy which is represented by a 2. For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your
program should return 3 because the closest enemy (2) is 3 spaces away from the 1.
The array will contain any number of 0's and 2's, but only a single 1.
It may not contain any 2's at all as well, where in that case your program should return a 0.
"""
def ArrayChallenge(arr):
    # Todo: your code goes here
    pass



"""
Q4. Dash Insert

String Challenge
Have the function StringChallenge(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
"""
def StringChallenge(str):
    # Todo: your code goes here
    pass


def testRecursionChallenge():
    print('Testing RecursionChallenge()...', end='')
    assert RecursionChallenge(4) == 24
    assert RecursionChallenge(5) == 120
    assert RecursionChallenge(6) == 720
    assert RecursionChallenge(7) == 5040
    assert RecursionChallenge(8) == 40320
    assert RecursionChallenge(9) == 362880
    assert RecursionChallenge(10) == 3628800
    assert RecursionChallenge(11) == 39916800
    assert RecursionChallenge(12) == 479001600
    assert RecursionChallenge(13) == 6227020800
    assert RecursionChallenge(14) == 87178291200
    assert RecursionChallenge(15) == 1307674368000
    assert RecursionChallenge(16) == 20922789888000
    assert RecursionChallenge(17) == 355687428096000
    assert RecursionChallenge(18) == 6402373705728000
    print('Passed!')


def testSetChallenge():
    print('Testing SetChallenge()...', end='')
    assert SetChallenge([1, 2, 3]) == 8
    assert SetChallenge([1, 2, 3, 4]) == 16
    assert SetChallenge([5, 6]) == 4
    assert SetChallenge([5, 6, 7]) == 8
    assert SetChallenge([5, 6, 7, 8]) == 16
    assert SetChallenge([5, 6, 7, 8, 9]) == 32
    assert SetChallenge([5, 6, 7, 8, 9, 10]) == 64
    assert SetChallenge([5, 6, 7, 8, 9, 10, 11]) == 128
    assert SetChallenge([5, 6, 7, 8, 9, 10, 11, 12]) == 256
    print('Passed!')


def testArrayChallenge():
    print('Testing ArrayChallenge()...', end='')
    assert ArrayChallenge([0, 0, 1, 0, 0, 2, 0, 2]) == 3
    assert ArrayChallenge([1, 0, 0, 0, 2, 2, 2]) == 4
    assert ArrayChallenge([2, 0, 0, 0, 2, 2, 1, 0]) == 1
    assert ArrayChallenge([0, 0, 0, 0, 0, 1, 0, 0, 0]) == 0
    assert ArrayChallenge([1, 0, 0, 0, 0, 0, 0]) == 0
    assert ArrayChallenge([1, 0, 0, 0, 0, 0, 2]) == 6
    assert ArrayChallenge([2, 0, 0, 0, 0, 0, 1]) == 6
    assert ArrayChallenge([0, 0, 0, 0, 0, 0, 1]) == 0
    print('Passed!')


def testStringChallenge():
    print('Testing StringChallenge()...', end='')
    assert StringChallenge('454793') == '4547-9-3'
    assert StringChallenge('1012356895') == '10123-5689-5'
    assert StringChallenge('99946') == '9-9-946'
    assert StringChallenge('56730') == '567-30'
    assert StringChallenge('0') == '0'
    assert StringChallenge('2745') == '2745'
    assert StringChallenge('2468') == '2468'
    assert StringChallenge('13579') == '1-3-5-7-9'
    assert StringChallenge('02468') == '02468'
    assert StringChallenge('1357913579') == '1-3-5-7-9-1-3-5-7-9'
    assert StringChallenge('0246813579') == '024681-3-5-7-9'
    assert StringChallenge('13579135790246813579') == '1-3-5-7-9-1-3-5-7-9024681-3-5-7-9'
    print('Passed!')


def testAll():
    # Comment out the tests you do not wish to run!
    testRecursionChallenge()
    testSetChallenge()
    testArrayChallenge()
    testStringChallenge()


def main():
    testAll()

if __name__ == '__main__':
    main()
