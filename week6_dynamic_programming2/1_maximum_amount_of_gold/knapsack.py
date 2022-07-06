# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w.sort(reverse = True)
    matrix = [[0 for j in range(W+1)] for i in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            matrix[i][j] = matrix[i-1][j]
            if w[i-1] <= j:
                val = matrix[i-1][j-w[i-1]] + w[i-1]
                if val > matrix[i][j]:
                    matrix[i][j] = val

    return matrix[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
