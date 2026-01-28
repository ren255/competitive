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


N, Q = LI()
A = LI()  # N
Q = [LI() for _ in range(Q)]


def swap(x):
    A[x - 1], A[x] = A[x], A[x - 1]
    # print(A)


def Sum(l, r):
    s = sum(A[l - 1 : r])
    print(s)


for query in Q:
    if query[0] == 1:
        swap(query[1])
    elif query[0] == 2:
        Sum(query[1], query[2])
