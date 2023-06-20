"""
Number System Conversion

Name: <your name>
"""

# Write functions to convert between decimal, binary, hexadecimal, and octal
# numbers.  Each function takes in a string representing a number in one
# number system and returns a string representing the number in another
# number system.
# Use lower case letters for the digits above 9, e.g., a = 10, b = 11, etc.


# Convert a decimal number to a binary number
def dec_to_bin(dec):
    # your code here
    pass


# Convert a binary number to a decimal number
def bin_to_dec(bin_str):
    # your code here
    pass


# Convert a decimal number to a hexadecimal number
def dec_to_hex(dec):
    # your code here
    pass


# Convert a hexadecimal number to a decimal number
def hex_to_dec(hex_str):
    # your code here
    pass


# Convert a decimal number to an octal number
def dec_to_oct(dec):
    # your code here
    pass


# Convert an octal number to a decimal number
def oct_to_dec(oct_str):
    # your code here
    pass


# Convert Octal to hexadecimal
def oct_to_hex(oct_str):
    # your code here
    pass


# Convert hexadecimal to octal
def hex_to_oct(hex_str):
    # your code here
    pass


def test_dec_to_bin():
    print('Testing dec_to_bin()...', end='')
    assert(dec_to_bin(0) == '0')
    assert(dec_to_bin(1) == '1')
    assert(dec_to_bin(2) == '10')
    assert(dec_to_bin(3) == '11')
    assert(dec_to_bin(5) == '101')
    assert(dec_to_bin(6) == '110')
    assert(dec_to_bin(7) == '111')
    assert(dec_to_bin(8) == '1000')
    assert(dec_to_bin(9) == '1001')
    assert(dec_to_bin(10) == '1010')
    assert(dec_to_bin(11) == '1011')
    assert(dec_to_bin(12) == '1100')
    assert(dec_to_bin(13) == '1101')
    assert(dec_to_bin(14) == '1110')
    assert(dec_to_bin(17) == '10001')
    assert(dec_to_bin(18) == '10010')
    assert(dec_to_bin(19) == '10011')
    assert(dec_to_bin(20) == '10100')
    assert(dec_to_bin(21) == '10101')
    assert(dec_to_bin(22) == '10110')
    assert(dec_to_bin(24) == '11000')
    assert(dec_to_bin(25) == '11001')
    assert(dec_to_bin(28) == '11100')
    assert(dec_to_bin(29) == '11101')
    assert(dec_to_bin(30) == '11110')
    assert(dec_to_bin(31) == '11111')
    assert(dec_to_bin(35) == '100011')
    assert(dec_to_bin(36) == '100100')
    assert(dec_to_bin(37) == '100101')
    assert(dec_to_bin(15502) == '11110010001110')
    assert(dec_to_bin(48392) == '1011110100001000')
    print('Passed.')


def test_bin_to_dec():
    print('Testing bin_to_dec()...', end='')
    assert(bin_to_dec('0') == 0)
    assert(bin_to_dec('1') == 1)
    assert(bin_to_dec('10') == 2)
    assert(bin_to_dec('11') == 3)
    assert(bin_to_dec('100') == 4)
    assert(bin_to_dec('101') == 5)
    assert(bin_to_dec('110') == 6)
    assert(bin_to_dec('111') == 7)
    assert(bin_to_dec('1000') == 8)
    assert(bin_to_dec('1001') == 9)
    assert(bin_to_dec('1010') == 10)
    assert(bin_to_dec('1011') == 11)
    assert(bin_to_dec('1100') == 12)
    assert(bin_to_dec('1101') == 13)
    assert(bin_to_dec('1110') == 14)
    assert(bin_to_dec('1111') == 15)
    assert(bin_to_dec('10000') == 16)
    assert(bin_to_dec('10001') == 17)
    assert(bin_to_dec('10010') == 18)
    assert(bin_to_dec('10011') == 19)
    assert(bin_to_dec('10100') == 20)
    assert(bin_to_dec('10101') == 21)
    assert(bin_to_dec('10110') == 22)
    assert(bin_to_dec('10111') == 23)
    assert(bin_to_dec('11000') == 24)
    assert(bin_to_dec('11001') == 25)
    assert(bin_to_dec('11010') == 26)
    assert(bin_to_dec('11011') == 27)
    assert(bin_to_dec('11100') == 28)
    assert(bin_to_dec('11101') == 29)
    assert(bin_to_dec('11110') == 30)
    assert(bin_to_dec('11111') == 31)
    assert(bin_to_dec('100000') == 32)
    assert(bin_to_dec('100001') == 33)
    assert(bin_to_dec('100010') == 34)
    assert(bin_to_dec('100011') == 35)
    assert(bin_to_dec('100100') == 36)
    assert(bin_to_dec('100101') == 37)
    assert(bin_to_dec('110110101101110') == 28014)
    print('Passed.')


def test_dec_to_hex():
    print('Testing dec_to_hex()...', end='')
    assert(dec_to_hex(0) == '0')
    assert(dec_to_hex(1) == '1')
    assert(dec_to_hex(2) == '2')
    assert(dec_to_hex(3) == '3')
    assert(dec_to_hex(4) == '4')
    assert(dec_to_hex(5) == '5')
    assert(dec_to_hex(6) == '6')
    assert(dec_to_hex(7) == '7')
    assert(dec_to_hex(8) == '8')
    assert(dec_to_hex(9) == '9')
    assert(dec_to_hex(10) == 'a')
    assert(dec_to_hex(11) == 'b')
    assert(dec_to_hex(12) == 'c')
    assert(dec_to_hex(13) == 'd')
    assert(dec_to_hex(14) == 'e')
    assert(dec_to_hex(15) == 'f')
    assert(dec_to_hex(16) == '10')
    assert(dec_to_hex(17) == '11')
    assert(dec_to_hex(18) == '12')
    assert(dec_to_hex(19) == '13')
    assert(dec_to_hex(20) == '14')
    assert(dec_to_hex(21) == '15')
    assert(dec_to_hex(22) == '16')
    assert(dec_to_hex(23) == '17')
    assert(dec_to_hex(24) == '18')
    assert(dec_to_hex(25) == '19')
    assert(dec_to_hex(26) == '1a')
    assert(dec_to_hex(27) == '1b')
    assert(dec_to_hex(28) == '1c')
    assert(dec_to_hex(29) == '1d')
    assert(dec_to_hex(30) == '1e')
    assert(dec_to_hex(31) == '1f')
    assert(dec_to_hex(32) == '20')
    assert(dec_to_hex(33) == '21')
    assert(dec_to_hex(34) == '22')
    assert(dec_to_hex(35) == '23')
    assert(dec_to_hex(36) == '24')
    assert(dec_to_hex(37) == '25')
    assert(dec_to_hex(3493858) == '354fe2')
    assert(dec_to_hex(125838) == '1eb8e')
    print('Passed.')


def test_hex_to_dec():
    print('Testing hex_to_dec()...', end='')
    assert(hex_to_dec('0') == 0)
    assert(hex_to_dec('1') == 1)
    assert(hex_to_dec('2') == 2)
    assert(hex_to_dec('3') == 3)
    assert(hex_to_dec('4') == 4)
    assert(hex_to_dec('5') == 5)
    assert(hex_to_dec('6') == 6)
    assert(hex_to_dec('7') == 7)
    assert(hex_to_dec('8') == 8)
    assert(hex_to_dec('9') == 9)
    assert(hex_to_dec('A') == 10)
    assert(hex_to_dec('B') == 11)
    assert(hex_to_dec('C') == 12)
    assert(hex_to_dec('D') == 13)
    assert(hex_to_dec('E') == 14)
    assert(hex_to_dec('F') == 15)
    assert(hex_to_dec('10') == 16)
    assert(hex_to_dec('11') == 17)
    assert(hex_to_dec('12') == 18)
    assert(hex_to_dec('13') == 19)
    assert(hex_to_dec('14') == 20)
    assert(hex_to_dec('15') == 21)
    assert(hex_to_dec('16') == 22)
    assert(hex_to_dec('17') == 23)
    assert(hex_to_dec('18') == 24)
    assert(hex_to_dec('19') == 25)
    assert(hex_to_dec('1A') == 26)
    assert(hex_to_dec('1B') == 27)
    assert(hex_to_dec('1C') == 28)
    assert(hex_to_dec('1D') == 29)
    assert(hex_to_dec('1E') == 30)
    assert(hex_to_dec('1F') == 31)
    assert(hex_to_dec('20') == 32)
    assert(hex_to_dec('21') == 33)
    assert(hex_to_dec('22') == 34)
    assert(hex_to_dec('23') == 35)
    assert(hex_to_dec('24') == 36)
    assert(hex_to_dec('25') == 37)
    assert(hex_to_dec('26') == 38)
    assert(hex_to_dec('27') == 39)
    assert(hex_to_dec('35522') == 218402)
    assert(hex_to_dec('1F96E') == 129390)
    print('Passed.')


def test_dec_to_oct():
    print('Testing dec_to_oct()...', end='')
    assert(dec_to_oct(0) == '0')
    assert(dec_to_oct(1) == '1')
    assert(dec_to_oct(2) == '2')
    assert(dec_to_oct(3) == '3')
    assert(dec_to_oct(4) == '4')
    assert(dec_to_oct(5) == '5')
    assert(dec_to_oct(6) == '6')
    assert(dec_to_oct(7) == '7')
    assert(dec_to_oct(8) == '10')
    assert(dec_to_oct(9) == '11')
    assert(dec_to_oct(10) == '12')
    assert(dec_to_oct(11) == '13')
    assert(dec_to_oct(12) == '14')
    assert(dec_to_oct(13) == '15')
    assert(dec_to_oct(14) == '16')
    assert(dec_to_oct(15) == '17')
    assert(dec_to_oct(16) == '20')
    assert(dec_to_oct(17) == '21')
    assert(dec_to_oct(18) == '22')
    assert(dec_to_oct(19) == '23')
    assert(dec_to_oct(20) == '24')
    assert(dec_to_oct(21) == '25')
    assert(dec_to_oct(22) == '26')
    assert(dec_to_oct(23) == '27')
    assert(dec_to_oct(24) == '30')
    assert(dec_to_oct(25) == '31')
    assert(dec_to_oct(26) == '32')
    assert(dec_to_oct(27) == '33')
    assert(dec_to_oct(28) == '34')
    assert(dec_to_oct(29) == '35')
    assert(dec_to_oct(30) == '36')
    assert(dec_to_oct(31) == '37')
    assert(dec_to_oct(32) == '40')
    assert(dec_to_oct(33) == '41')
    assert(dec_to_oct(34) == '42')
    assert(dec_to_oct(35) == '43')
    assert(dec_to_oct(36) == '44')
    assert(dec_to_oct(37) == '45')
    assert(dec_to_oct(38) == '46')
    assert(dec_to_oct(39) == '47')
    assert(dec_to_oct(4985823) == '23011737')
    assert(dec_to_oct(125838) == '365616')
    print('Passed.')


def test_oct_to_dec():
    print('Testing oct_to_dec()...', end='')
    assert(oct_to_dec('0') == 0)
    assert(oct_to_dec('1') == 1)
    assert(oct_to_dec('2') == 2)
    assert(oct_to_dec('3') == 3)
    assert(oct_to_dec('4') == 4)
    assert(oct_to_dec('5') == 5)
    assert(oct_to_dec('6') == 6)
    assert(oct_to_dec('7') == 7)
    assert(oct_to_dec('10') == 8)
    assert(oct_to_dec('11') == 9)
    assert(oct_to_dec('12') == 10)
    assert(oct_to_dec('13') == 11)
    assert(oct_to_dec('14') == 12)
    assert(oct_to_dec('15') == 13)
    assert(oct_to_dec('16') == 14)
    assert(oct_to_dec('17') == 15)
    assert(oct_to_dec('20') == 16)
    assert(oct_to_dec('21') == 17)
    assert(oct_to_dec('22') == 18)
    assert(oct_to_dec('23') == 19)
    assert(oct_to_dec('24') == 20)
    assert(oct_to_dec('25') == 21)
    assert(oct_to_dec('26') == 22)
    assert(oct_to_dec('27') == 23)
    assert(oct_to_dec('30') == 24)
    assert(oct_to_dec('31') == 25)
    assert(oct_to_dec('32') == 26)
    assert(oct_to_dec('33') == 27)
    assert(oct_to_dec('34') == 28)
    assert(oct_to_dec('35') == 29)
    assert(oct_to_dec('36') == 30)
    assert(oct_to_dec('37') == 31)
    assert(oct_to_dec('40') == 32)
    assert(oct_to_dec('41') == 33)
    assert(oct_to_dec('42') == 34)
    assert(oct_to_dec('43') == 35)
    assert(oct_to_dec('44') == 36)
    assert(oct_to_dec('435231') == 146073)
    assert(oct_to_dec('374476') == 129342)
    print('Passed.')


def test_oct_to_hex():
    print('Testing oct_to_hex()...', end='')
    assert(oct_to_hex('0') == '0')
    assert(oct_to_hex('1') == '1')
    assert(oct_to_hex('2') == '2')
    assert(oct_to_hex('3') == '3')
    assert(oct_to_hex('4') == '4')
    assert(oct_to_hex('5') == '5')
    assert(oct_to_hex('6') == '6')
    assert(oct_to_hex('7') == '7')
    assert(oct_to_hex('10') == '8')
    assert(oct_to_hex('11') == '9')
    assert(oct_to_hex('12') == 'a')
    assert(oct_to_hex('13') == 'b')
    assert(oct_to_hex('14') == 'c')
    assert(oct_to_hex('15') == 'd')
    assert(oct_to_hex('16') == 'e')
    assert(oct_to_hex('17') == 'f')
    assert(oct_to_hex('20') == '10')
    assert(oct_to_hex('21') == '11')
    assert(oct_to_hex('22') == '12')
    assert(oct_to_hex('23') == '13')
    assert(oct_to_hex('24') == '14')
    assert(oct_to_hex('25') == '15')
    assert(oct_to_hex('26') == '16')
    assert(oct_to_hex('27') == '17')
    assert(oct_to_hex('30') == '18')
    assert(oct_to_hex('31') == '19')
    assert(oct_to_hex('32') == '1a')
    assert(oct_to_hex('33') == '1b')
    assert(oct_to_hex('34') == '1c')
    assert(oct_to_hex('35') == '1d')
    assert(oct_to_hex('36') == '1e')
    assert(oct_to_hex('37') == '1f')
    assert(oct_to_hex('40') == '20')
    assert(oct_to_hex('41') == '21')
    assert(oct_to_hex('42') == '22')
    assert(oct_to_hex('43') == '23')
    assert(oct_to_hex('44') == '24')
    assert(oct_to_hex('435231') == '23a99')
    assert(oct_to_hex('374476') == '1f93e')
    print('Passed.')



def test_hex_to_oct():
    print('Testing hex_to_oct()...', end='')
    assert(hex_to_oct('0') == '0')
    assert(hex_to_oct('1') == '1')
    assert(hex_to_oct('2') == '2')
    assert(hex_to_oct('3') == '3')
    assert(hex_to_oct('4') == '4')
    assert(hex_to_oct('5') == '5')
    assert(hex_to_oct('6') == '6')
    assert(hex_to_oct('7') == '7')
    assert(hex_to_oct('8') == '10')
    assert(hex_to_oct('9') == '11')
    assert(hex_to_oct('A') == '12')
    assert(hex_to_oct('B') == '13')
    assert(hex_to_oct('C') == '14')
    assert(hex_to_oct('D') == '15')
    assert(hex_to_oct('E') == '16')
    assert(hex_to_oct('F') == '17')
    assert(hex_to_oct('10') == '20')
    assert(hex_to_oct('11') == '21')
    assert(hex_to_oct('12') == '22')
    assert(hex_to_oct('13') == '23')
    assert(hex_to_oct('14') == '24')
    assert(hex_to_oct('15') == '25')
    assert(hex_to_oct('16') == '26')
    assert(hex_to_oct('17') == '27')
    assert(hex_to_oct('18') == '30')
    assert(hex_to_oct('19') == '31')
    assert(hex_to_oct('1A') == '32')
    assert(hex_to_oct('1B') == '33')
    assert(hex_to_oct('1C') == '34')
    assert(hex_to_oct('1D') == '35')
    assert(hex_to_oct('1E') == '36')
    assert(hex_to_oct('1F') == '37')
    assert(hex_to_oct('20') == '40')
    assert(hex_to_oct('21') == '41')
    assert(hex_to_oct('22') == '42')
    assert(hex_to_oct('23') == '43')
    assert(hex_to_oct('24') == '44')
    assert(hex_to_oct('435231') == '20651061')
    assert(hex_to_oct('374476') == '15642166')
    print('Passed.')


def test_all():
    test_dec_to_bin()
    test_bin_to_dec()
    test_dec_to_hex()
    test_hex_to_dec()
    test_dec_to_oct()
    test_oct_to_dec()
    test_oct_to_hex()
    test_hex_to_oct()


if __name__ == '__main__':
    test_all()