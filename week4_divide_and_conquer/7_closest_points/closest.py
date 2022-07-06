#Uses python3
import sys
import math

import copy


# 求a，b两点间的距离
def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def find_nearest_points(points_x, points_y, n):
    # 边界条件
    if n == 2:
        return [distance(points_x[0], points_x[1]), [points_x[0], points_x[1]]]
    if n == 1:
        return [999, [points_x[0]], points_x[0]]

    #  将点集对半分
    left_points = points_x[0:int(n / 2)]
    right_points = points_x[int(n / 2):n + 1]
    lx = (points_x[int(n / 2)][0] + points_x[int(n / 2) - 1][0]) / 2  # 中线横坐标

    d1 = find_nearest_points(left_points, points_y, int(n / 2))
    d2 = find_nearest_points(right_points, points_y, int(n / 2) + (n % 2))

    min_set = min(d1, d2, key=lambda x: x[0])
    min_points = min_set[1]

    # print("d = %f" % min_set[0])

    # print('lx = %f' % lx)
    T = []

    for i in points_y:
        if lx - min_set[0] <= i[0] <= lx + min_set[0]:
            T.append(i)
    # 计算T1中每个点到最多5个点的距离
    min_dis = min_set[0]
    for k in T:
        for i in range(1, 5):
            if T.index(k) + i <= len(T) - 1:
                if T[T.index(k) + i][1] - k[1] < min_set[0]:
                    dis = distance(k, T[T.index(k) + i])
                    if dis < min_dis:
                        min_dis = dis
                        min_points[0] = k
                        min_points[1] = T[T.index(k) + i]
                else:
                    break
            else:
                break
    return [min(min_dis, min_set[0]), min_points]


if __name__ == '__main__':


    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    a = list(zip(x,y))
    a.sort(key = lambda y: y[0])
    b = a
    a.sort(key=lambda y: y[1])
    c = a
    n=len(x)
    print("{0:.9f}".format(find_nearest_points(b,c,n)[0]))
