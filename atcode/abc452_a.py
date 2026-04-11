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


targets = [
    [1, 7],
    [3, 3],
    [5, 5],
    [7, 7],
    [9, 9],
]

M, D = LI()

for m, d in targets:
    if m == M and d == D:
        print("Yes")
        exit()

print("No")
