# Uses python3
import sys
#找第一个大于的index
def binary_search(A,  target):
    low,high = 0,len(A)-1
    while low <= high:
        mid = low + (high - low) // 2
        if target >= A[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low
#找第一个大于等于的index
def binary_search2(A,  target):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target > A[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))
def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts = merge_sort(starts)

    ends = merge_sort(ends)

    for k in range(len(points)):
        c = binary_search(starts,points[k])  #找到第一个大于他的

        d = binary_search2(ends,points[k])

        cnt[k] = c-d
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
