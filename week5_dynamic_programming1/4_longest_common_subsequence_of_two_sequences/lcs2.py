#Uses python3

import sys



def lcs2(str1, str2):
    matrix = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)] #怎么创建matrix
    for i in range(1,len(str1) + 1):
        for j in range(1,len(str2) + 1):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            if (str1[i - 1] == str2[j - 1]):
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[len(str1)][len(str2)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
