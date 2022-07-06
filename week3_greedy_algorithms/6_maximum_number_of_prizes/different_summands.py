# Uses python3
import sys

def optimal_summands(n):
    summands = []
    used = 0
    start = 1
    while used <= n:
        summands.append(start)
        used = used + start
        start += 1
        if n - used < start:
            summands[-1] = summands[-1] + n - used
            return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
