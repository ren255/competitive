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


N, T = LI()
A = LI()

A.insert(0, 0)
A.append(T)
total = 0
next_start = 0
for i in range(1, len(A)):
    between = A[i] - next_start
    # print(
    #     f"{i=}: {A[i-1]} ~ {A[i]} {next_start=} {total=}+{between} {A[i] > next_start}"
    # )
    if A[i] > next_start:
        total += between
        next_start = A[i] + 100

print(total)
