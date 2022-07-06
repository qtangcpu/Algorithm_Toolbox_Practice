# Uses python3
import sys

def fibonacci_sum_naive(n):
    a = [0, 1]
    for i in range(2, 63):
        a.append(a[i - 1] + a[i - 2])
    return a[n%60+2]%10 -1

def fibonacci_partial_sum_naive(from_, to):


    return (fibonacci_sum_naive(to) - fibonacci_sum_naive(from_-1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
