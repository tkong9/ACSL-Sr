import sys

def triangle(s, d, r):
    # base case
    if r == 1:
        return s
    # recursive case
    return triangle(s, d, r - 1) + d * (r - 1)


def triangle2(s, d, r):
    result = s
    for i in range(1, r):
        result += d * i
    return result


def decimal_to_octal(n):
    return oct(n)[2:]

def octal_to_decimal(n):
    return int(str(n), 8)

def sum_of_digits(n):
    return sum(map(int, str(n)))

def solve(s, d, r):
    first_num_of_last_row = triangle2(s, d, r)
    sum_of_last_row = 0
    for i in range(r):
        octal = decimal_to_octal(first_num_of_last_row)
        sum_of_last_row += sum_of_digits(octal)
        first_num_of_last_row += d

    return sum_of_last_row

if __name__ == '__main__':
    sys.stdin = open('triangle.txt')
    for tc in range(10):
        s, d, r = map(int, input().split())
        s = octal_to_decimal(s)
        d = octal_to_decimal(d)
        print(f'{tc + 1}. {solve(s, d, r)}')

