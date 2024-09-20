import sys

def octal_to_decimal(n):
    return int(str(n), 8)

def decimal_to_octal(n):
    return oct(n)[2:]

def solve(s, d, r):
    s = d * (r - 1) * r // 2 + s

    first_num_of_last_row = s
    sum_of_last_row = 0
    for i in range(r):
        octal = decimal_to_octal(first_num_of_last_row)
        sum_of_last_row += sum(map(int, octal))
        first_num_of_last_row += d

    return sum_of_last_row




if __name__ == '__main__':
    sys.stdin = open('triangle.txt')
    for tc in range(10):
        s, d, r = map(int, input().split())
        s = octal_to_decimal(s)
        d = octal_to_decimal(d)
        print(f'{tc + 1}. {solve(s, d, r)}')
