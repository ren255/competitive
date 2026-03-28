import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


Q = I()

querys = [LI() for _ in range(Q)]

import sortedcontainers
from bisect import bisect_left

trees = sortedcontainers.SortedList()


for query in querys:
    if query[0] == 1:
        trees.add(query[1])
    else:
        idx = bisect_left(trees, query[1] + 1)
        del trees[:idx]

    print(len(trees))
