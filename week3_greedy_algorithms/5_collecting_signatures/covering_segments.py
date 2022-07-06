# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort()
    number_covered = 0
    while len(segments)  > 0 :
        point = 1000000000000
        for segment in segments:
            point = min(point, segment[1] )
        segments = [x for x in segments if x[0] > point]
        points.append(point)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
