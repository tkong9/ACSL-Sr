'''
Lex Strings

Name: <your name>
'''
#
# Complete the 'rearrangedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#

def rearrangedString(s):
    s = ''.join(ch for ch in s if ch.isalnum())
    newS = s.replace(" ", "")
    letters = []
    current = 1
    for i in newS:
        for j in range(newS.index(i) + 1, len(newS)):
            if (i == newS[j:j + 1]):
                current = current + 1
        letters.append(i)
        letters.append(current)
        current = 1

    m = 0
    output = ""
    num = len(letters) / 2
    num = int(num)
    for x in range(0, num):
        smallList = []
        m = maxOfList(letters)
        if (m == 0):
            break
        c = letters.count(m)
        if (x % 2 == 0):
            for times in range(0, c):
                indexOf = letters.index(m)
                le = letters[indexOf - 1:indexOf]
                if (smallList.count(le) == 0):
                    if (len(smallList) == 0):
                        smallList.append(le)
                    else:
                        for l in smallList:
                            if (le < l):
                                smallList.insert(smallList.index(l), le)
                                break
                            if (smallList.index(l) == len(smallList) - 1):
                                smallList.append(le)
                                break
                letters.pop(indexOf)
                letters.pop(indexOf - 1)
        else:
            for times in range(0, c):
                indexOf = letters.index(m)
                le = letters[indexOf - 1:indexOf]
                if (smallList.count(le) == 0):
                    if (len(smallList) == 0):
                        smallList.append(le)
                    else:
                        for l in smallList:
                            if (le > l):
                                smallList.insert(smallList.index(l), le)
                                break
                            if (smallList.index(l) == len(smallList) - 1):
                                smallList.append(le)
                                break
                letters.pop(indexOf)
                letters.pop(indexOf - 1)
        st = ""
        for s in smallList:
            for r in s:
                st = st + r
        if (m == 1):
            output = output + str(m) + st
        else:
            output = output + str(m) + st + ","
        st = ""
    return output


def maxOfList(list):
    max = 0
    for p in list:
        if (type(p) == int):
            if (p > max):
                max = p
    return max


if __name__ == '__main__':
    import sys
    sys.stdin = open('lex_strings_sample_data.txt', 'r')
    for tc in range(10):
        s = input()
        result = rearrangedString(s)
        print('Test Case #{}: {}'.format(tc + 1, result))


'''
Your output on console should be:
Test Case #1: 6in,4ts,3aegr,2o,1ESTfhlmpx
Test Case #2: 5a,4se,3r,2tonkihc,1ACFHLRSdflmuwy
Test Case #3: 2135ei,1tsrohgfdaTPI9642
Test Case #4: 7es,4lh,2a,1ytrobS
Test Case #5: 8a,5n,4gu,3rlic,2CPSdehmosty,1vbVRJIBA
Test Case #6: 7ae,6ni,5t,4rhd,3gl,2vsoc,119CDIOVbmpuwy
Test Case #7: 9e,5nica,4or,3th,202CTsu,1vpmlfdSA
Test Case #8: 53,472,345689deo,2trni1,1IPTafghsu
Test Case #9: 14e,13p,7i,6r,5cdk,4P,2alost,1ywnmfH
Test Case #10: 8o,7e,5hn,3wtsrda,2ikp,1ylfbT10
'''
