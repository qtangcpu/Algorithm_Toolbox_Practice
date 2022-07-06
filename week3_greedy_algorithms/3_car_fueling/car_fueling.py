# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    numrefill = 0
    currentrefill = 0
    stops.append(d)
    stops.insert(0,0)
    while currentrefill <= n:
        lastrefill = currentrefill
        while (currentrefill <= n and stops[currentrefill+1] - stops[lastrefill] <= tank):
            currentrefill = currentrefill+1
        if currentrefill == lastrefill:
            return -1
        if currentrefill <= n:
            numrefill = numrefill +1

    return numrefill

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
