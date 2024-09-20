import sys


# Function to generate the numbers in the triangle with memoization using a list
def triangle(s, d, r, memo):
    if memo[r] is not None:  # If the result is already computed, use it
        return memo[r]

    # base case
    if r == 1:
        memo[r] = s  # Save the result in memo list
        return s

    # recursive case
    result = triangle(s, d, r - 1, memo) + d * (r - 1)
    memo[r] = result  # Save the computed result in the memo list
    return result


def decimal_to_octal(n):
    """Convert a decimal number to its octal representation as a string."""
    return oct(n)[2:]


def octal_to_decimal(n):
    """Convert an octal number (given as an integer) to decimal."""
    return int(str(n), 8)


def sum_of_digits(n):
    """Return the sum of digits of a given number."""
    return sum(map(int, str(n)))


def solve(s, d, r):
    """Solve the problem by calculating the sum of digits on the r-th row."""
    memo = [None] * (r + 1)  # Create a memo list with None values, size r+1
    first_num_of_last_row = triangle(s, d, r, memo)

    sum_of_last_row = 0
    for i in range(r):
        octal = decimal_to_octal(first_num_of_last_row)
        sum_of_last_row += sum_of_digits(octal)
        first_num_of_last_row += d  # Move to the next number in the row

    return sum_of_last_row


if __name__ == '__main__':
    sys.stdin = open('triangle.txt')
    for tc in range(10):
        s, d, r = map(int, input().split())
        s = octal_to_decimal(s)
        d = octal_to_decimal(d)
        print(f'{tc + 1}. {solve(s, d, r)}')
