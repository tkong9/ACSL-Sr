"""
Triangle Number

Name: <your name>
"""

"""
Triangle Number is a number that can be represented as a triangle with dots arranged in rows with one dot in the first row,
two dots in the second row, three dots in the third row, and so on.

Triangle Number has the following steps:
    1. Start from the first row.
    2. Add one dot to the next row.
    3. Repeat step 2 until the desired number of rows is reached.
    4. Count the total number of dots in all rows.
    5. Return the total number of dots.

Triangle Number has a time complexity of O(n) where n is the number of rows.
Triangle Number has a space complexity of O(1) because it does not use any additional space.

Visualize Triangle Number: https://www.mathsisfun.com/algebra/triangular-numbers.html

Complete the 'triangle_number' function below.
"""


def triangle_number(n):
    """
    Compute the nth triangular number.

    This function uses a recursive approach to compute the nth triangular number.
    A triangular number counts the objects that can form an equilateral triangle.
    The nth triangular number is the number of dots composing a triangle with n dots on a side,
    and it represents the sum of the n natural numbers from 1 to n.
    Visualize Triangle Number: https://www.mathsisfun.com/algebra/triangular-numbers.html

    Parameters:
    n (int): The number to compute the triangular number of.

    Returns:
    int: The nth triangular number.
    """
    # TODO: Write your code here
    pass


def test_triangle_number():
    print('Testing triangle_number()...', end='')
    assert triangle_number(0) == 0
    assert triangle_number(1) == 1
    assert triangle_number(2) == 3
    assert triangle_number(3) == 6
    assert triangle_number(4) == 10
    assert triangle_number(5) == 15
    assert triangle_number(6) == 21
    assert triangle_number(7) == 28
    assert triangle_number(8) == 36
    assert triangle_number(9) == 45
    assert triangle_number(10) == 55
    assert triangle_number(11) == 66
    assert triangle_number(12) == 78
    assert triangle_number(13) == 91
    assert triangle_number(14) == 105
    assert triangle_number(15) == 120
    assert triangle_number(16) == 136
    assert triangle_number(17) == 153
    assert triangle_number(18) == 171
    assert triangle_number(19) == 190
    assert triangle_number(20) == 210
    assert triangle_number(21) == 231
    assert triangle_number(22) == 253
    assert triangle_number(23) == 276
    assert triangle_number(24) == 300
    assert triangle_number(25) == 325
    assert triangle_number(26) == 351
    assert triangle_number(27) == 378
    assert triangle_number(28) == 406
    assert triangle_number(29) == 435
    assert triangle_number(30) == 465
    assert triangle_number(31) == 496
    assert triangle_number(32) == 528
    assert triangle_number(33) == 561
    assert triangle_number(34) == 595
    assert triangle_number(35) == 630
    assert triangle_number(36) == 666
    assert triangle_number(37) == 703
    assert triangle_number(38) == 741
    assert triangle_number(39) == 780
    assert triangle_number(40) == 820
    assert triangle_number(41) == 861
    assert triangle_number(42) == 903
    assert triangle_number(43) == 946
    assert triangle_number(44) == 990
    print("All test cases passed!")


if __name__ == "__main__":
    test_triangle_number()
