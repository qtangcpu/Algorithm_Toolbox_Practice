# Uses python3
import sys

def optimal_sequence(n):
    #还是要dynamic programing
    #先创建一个空list，记录每一步的最少，from bottom to top
    result = []
    v = [0]*n
    for i in range(2,n+1):
        if i% 3 == 0 and i % 2 == 0:
            v[i-1] = min(v[int(i/2)-1] +1, v[int(i/3)-1] +1, v[i-2]+1)
        elif i% 3 == 0 and i % 2 != 0:
            v[i-1] = min( v[int(i / 3)-1] + 1, v[i-2] +1)
        elif i % 2 == 0 and i % 3 != 0:
            v[i-1] = min(v[int(i / 2)-1] + 1, v[i-2] +1)
        elif i % 2 != 0 and i % 3 != 0:
            v[i-1] = v[i-2] +1
    j = n
    result.append(int(j))
    while j >1:
        if v[int(j-2)] == v[int(j-1)] -1:
            j = j-1

        elif j % 2 == 0 and v[int(j/2) -1] == v[int(j-1)] - 1:
            j = j / 2

        elif j % 3 == 0 and v[int(j/3) -1] == v[int(j-1)] - 1:
            j = j/ 3

        result.append(int(j))
    return reversed(result)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

