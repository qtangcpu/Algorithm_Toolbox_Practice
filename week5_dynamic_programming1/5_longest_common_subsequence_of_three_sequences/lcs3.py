#Uses python3

import sys

def lcs3(str1, str2, str3):
    matrix = [[[0 for k in range(len(str3) + 1)] for j in range(len(str2) + 1)] for i in range(len(str1) + 1)] # 怎么创建matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            for k in range(1, len(str3)+1):
                if i == 0 and j == 0 and k == 0:
                    matrix[i][j][k] = 0
                if (str1[i - 1] == str2[j - 1]) and (str1[i - 1] == str3[k - 1]) and (str2[j - 1] == str3[k - 1]):
                    matrix[i][j][k] = matrix[i - 1][j - 1][k -1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k],matrix[i][j][k-1])
    return matrix[len(str1)][len(str2)][len(str3)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
