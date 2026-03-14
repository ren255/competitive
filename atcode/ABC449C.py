import bisect, collections, copy, heapq, itertools, math, string
import sys


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


from collections import defaultdict

N, L, R = LI()
S = S()

pos = defaultdict(list)
for i, c in enumerate(S):
    pos[c].append(i)

from bisect import bisect_left, bisect_right

count = 0
for indices in pos.values():
    for k, i in enumerate(indices):
        lo = bisect_left(indices, i + L, k + 1)
        hi = bisect_right(indices, i + R, k + 1)
        count += hi - lo

print(count)
