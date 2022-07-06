#Uses python3

import sys

def is_greater_or_equeal(maxDigit,digit):
    a = [str(maxDigit),str(digit)]
    a.sort(key=lambda x: len(x))
    for i in range( len(a[0]) ):
        if a[0][i] <  a[1][i]:
            return False
    return True

def max_value(maxDigit,digit):
    #a = [str(maxDigit),str(digit)]
    #a.sort(key=lambda x: len(x))
    '''
    for i in range(len(a[1])):
        if a[0][i % len(a[0])] < a[1][i]:
            return a[1]
        elif a[0][i % len(a[0])] > a[1][i]:
            return a[0]
        '''
    max_first = str(maxDigit) + str(digit)
    digit_first = str(digit) +str(maxDigit)
    if  max_first > digit_first:
        return maxDigit
    else:
        return digit
    #return a[0]

def largest_number(a):
    res = ""
    while len(a) > 0:
        maxDigit = 0
        for digit in a:
            maxDigit = max_value(maxDigit,digit)
        res =res +str(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':

    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

