# Uses python3
import sys

def find_period(n,m):
    a0, a1 = 0,1
    for i in range(m*m):
        a0,a1 = a1, (a0+a1) % m
        if (a0==0 and a1 == 1):
            return i+1

def get_fibonacci_huge_naive(n, m):
    p = find_period(n,m)
    n = n % p
    a0 = 0
    a1 = 1
    if n == 0:
        return a0
    elif n ==1:
        return a1
    else:
        for i in range(2,n+1):
            a0, a1 = a1, (a0 + a1)
    return a1 % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
