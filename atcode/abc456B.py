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


A = [LI() for _ in range(3)]

target = {4, 5, 6}
count = 0  # 有利な場合の数

for j0 in range(6):
    for j1 in range(6):
        for j2 in range(6):
            vals = [A[0][j0], A[1][j1], A[2][j2]]
            if sorted(vals) == [4, 5, 6]:
                count += 1

prob = count / 6**3

print(prob)
