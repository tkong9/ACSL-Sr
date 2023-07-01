"""
Fibonacci sequence
"""

"""
Fibonacci sequence is a sequence of numbers where the next number is the sum of the previous two numbers.
The first two numbers of the Fibonacci sequence are 0 and 1.
The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def fibonacci(n):
    """
    Compute the nth Fibonacci number.

    This function uses a recursive approach to compute the nth Fibonacci number.
    The Fibonacci sequence is a series of numbers in which each number is the sum
    of the two preceding ones, usually starting with 0 and 1.

    Note: This function has a high time complexity for large values of n due to
    redundant computations. For large n, consider using a dynamic programming
    approach or storing previously computed values.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci():
    print("Testing fibonacci()...", end="")
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13
    assert fibonacci(9) == 21
    assert fibonacci(10) == 34
    assert fibonacci(11) == 55
    assert fibonacci(12) == 89
    assert fibonacci(13) == 144
    assert fibonacci(14) == 233
    assert fibonacci(15) == 377
    assert fibonacci(16) == 610
    assert fibonacci(17) == 987
    assert fibonacci(18) == 1597
    assert fibonacci(19) == 2584
    assert fibonacci(20) == 4181
    assert fibonacci(21) == 6765
    assert fibonacci(22) == 10946
    assert fibonacci(23) == 17711
    assert fibonacci(24) == 28657
    assert fibonacci(25) == 46368
    assert fibonacci(26) == 75025
    assert fibonacci(27) == 121393
    assert fibonacci(28) == 196418
    assert fibonacci(29) == 317811
    assert fibonacci(30) == 514229
    print("Passed!")


if __name__ == "__main__":
    test_fibonacci()