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


N = I()
T = LI()

t = T.copy()
a1 = min(t)
t.remove(a1)
a2 = min(t)
t.remove(a2)
a3 = min(t)
t.remove(a3)

print(T.index(a1) + 1, T.index(a2) + 1, T.index(a3) + 1)
