# Uses python3
import sys

def get_majority_element(a, left, right):
    b = {}
    for i in range(right):
        if a[i] in b:
            b[a[i]] +=1
        else:
            b[a[i]] = 1
    for i in b:
        if b[i] > right/2:
            return 0
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
