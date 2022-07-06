# Uses python3
import sys

import itertools
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(numbers,op):

    m_matrix = [[0 for j in range(len(numbers))] for i in range(len(numbers))]
    M_matrix = [[0 for j in range(len(numbers))] for i in range(len(numbers))]
    for i in range(len(numbers)):
        m_matrix[i][i] = numbers[i]
        M_matrix[i][i] = numbers[i]


    for s in range(1,len(numbers)):
        for i in range(len(numbers)-s):
            j = i + s
            m = sys.maxsize
            M = -sys.maxsize
            for k in range(i,j):
                a = evalt(M_matrix[i][k],M_matrix[k+1][j], op[k])
                b = evalt(M_matrix[i][k], m_matrix[k + 1][j], op[k])
                c = evalt(m_matrix[i][k], M_matrix[k + 1][j], op[k])
                d = evalt(m_matrix[i][k], m_matrix[k + 1][j], op[k])
                if min(a,b,c,d) < m:
                    m = min(a,b,c,d)
                if max(a,b,c,d) > M:
                    M = max(a,b,c,d)
            m_matrix[i][j] = m
            M_matrix[i][j] = M
    return M_matrix[0][len(numbers)-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    a = list(input)
    numbers = list(map(int, a[0::2]))
    op = a[1::2]
    print(get_maximum_value(numbers,op))
