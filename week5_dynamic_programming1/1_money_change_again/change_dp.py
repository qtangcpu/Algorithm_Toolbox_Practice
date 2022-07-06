# Uses python3
import sys

def get_change(m):
    min_change = [0]*(m+1)
    dom = [1,3,4]
    for i in range(1,m+1):
        min_change[i] = float('inf')
        for j in dom:
            if i >= j:
                NumCoins = min_change[i-j] + 1
                if NumCoins < min_change[i]:
                    min_change[i] = NumCoins
    return min_change[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
