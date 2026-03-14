import bisect, collections, copy, heapq, itertools, math, string
import numpy as np
import sys


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


L, R, D, U = LI()


def is_black(x, y):
    return max(abs(x), abs(y)) % 2 == 0


# L≤x≤R かつ D≤y≤U

pairs = []
ctn = 0
for i in range(L, R + 1):
    for j in range(D, U + 1):
        if max(abs(i), abs(j)) % 2 == 0:
            ctn += 1
print(ctn)

# print(len(range(L, R + 1)), len(range(D, U + 1)))
