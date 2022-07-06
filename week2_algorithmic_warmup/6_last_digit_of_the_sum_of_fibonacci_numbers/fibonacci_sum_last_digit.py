# Uses python3
import sys

'''def fibonacci_sum_naive(n):
    if n <= 2:
        return n
    forward_3place = 0
    forward_2place = 1
    forward_1place = 2

    for _ in range(n-2):
         forward_1place, forward_2place, forward_3place\
            = (forward_1place*2 - forward_3place) % 10, forward_1place, forward_2place

    return forward_1place
'''
def fibonacci_sum_naive(n):
    a = [0, 1]
    for i in range(2, n%60+3):
        a.append(a[i - 1] + a[i - 2])
    return (a[n%60+2]%10 -1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))


#从n=3开始，当前数字等于n3 = （n3-1）*2 - n3-4


