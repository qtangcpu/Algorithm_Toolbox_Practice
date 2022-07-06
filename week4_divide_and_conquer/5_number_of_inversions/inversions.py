import sys


def get_number_of_inversions(a, b, left, right):
    '''
    def merge_sort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        result= marge1(merge_sort(left), merge_sort(right))
        return result

    def marge1(left, right):
        result = []
        count = 0
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                count += 1
        result += left
        result += right
        return result
'''
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    result = []
    l = a[left:ave]
    r = a[ave:right]
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
            number_of_inversions += len(l)
    result += l
    result += r
    a[left:right] = result
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
