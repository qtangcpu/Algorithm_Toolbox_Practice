# Uses python3
from sys import stdin


def find_period(m):
    a0, a1 = 0,1
    l0, l1 = 0,1
    for i in range(m*m):
        l0 = (a1*(a1+a0))%10
        a0,a1 = a1, a0+a1
        l1 = (a1 * (a1 + a0))%10
        if (l0==0 and l1 == 1):
            return i+1

def fibonacci_sum_squares_naive(n):
    n = n % find_period(10)
    a0, a1 = 0, 1
    l0, l1 = 0, 1
    if n == 0:
        return l0
    if n == 1:
        return l1
    for i in range(n-1):
        l0 = (a1 * (a1 + a0)) % 10
        a0, a1 = a1, a0 + a1
        l1 = (a1 * (a1 + a0)) % 10
    return l1

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
