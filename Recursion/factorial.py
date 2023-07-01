"""
Factorial of a number using recursion
"""

"""
Factorial is the product of all positive integers less than or equal to n.
The factorial of n is denoted by n!.

The factorial of 0 is 1. 0 = 1 
The factorial of 1 is 1. 1 = 1 * 1
The factorial of 2 is 2. 2 = 2 * 1
The factorial of 3 is 6. 6 = 3 * 2 * 1
The factorial of 4 is 24. 24 = 4 * 3 * 2 * 1
The factorial of 5 is 120. 120 = 5 * 4 * 3 * 2 * 1
"""

def factorial(n):
    """
    Compute the factorial of a number.

    This function uses a recursive approach to compute the factorial of a number.
    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted by n!.

    Parameters:
    n (int): The number to compute the factorial of.

    Returns:
    int: The factorial of the number n.
    """
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def test_factorial():
    print("Testing factorial()...", end="")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(9) == 362880
    assert factorial(10) == 3628800
    assert factorial(11) == 39916800
    assert factorial(12) == 479001600
    assert factorial(13) == 6227020800
    assert factorial(14) == 87178291200
    assert factorial(15) == 1307674368000
    assert factorial(16) == 20922789888000
    assert factorial(17) == 355687428096000
    assert factorial(18) == 6402373705728000
    assert factorial(19) == 121645100408832000
    print("Passed!")


if __name__ == "__main__":
    test_factorial()