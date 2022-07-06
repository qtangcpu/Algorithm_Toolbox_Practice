def binary_search(keys, query, l, r):

    while l <= r:
        m = (l + r + 1) // 2
        if query == keys[m]:
            return m
        elif query > keys[m]:
            l = m + 1
        elif query < keys[m]:
            r = m - 1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    l = 0
    r = len(input_keys)-1
    for q in input_queries:
        print(binary_search(input_keys, q, l, r ), end=' ')
