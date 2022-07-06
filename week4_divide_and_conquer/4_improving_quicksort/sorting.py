# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m_l = l
    m_r = l
    i = l+1
    while i <= r:
        if a[i] < x:
            #a.insert(l,a.pop(i))
            a[i],a[m_l],a[m_r+1] = a[m_r+1],a[i],a[m_l]
            i += 1
            m_l += 1
            m_r += 1
        elif a[i] == x:
            a[i],a[m_r+1] = a[m_r+1],a[i]
            m_r += 1
            i += 1
        elif a[i] > x:
            i += 1
    return m_l, m_r




def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m_l, m_r = partition3(a, l, r)
    randomized_quick_sort(a, l, m_l - 1);
    randomized_quick_sort(a, m_r + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
