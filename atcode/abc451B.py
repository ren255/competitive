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


N, M = LI()

majors = [LI() for _ in range(N)]

# print(majors)

from collections import defaultdict

pplA = defaultdict(int)
pplB = defaultdict(int)

for a, b in majors:
    pplA[a] += 1
    pplB[b] += 1

# print(pplA)
# print(pplB)

for i in range(1, M + 1):
    print(pplB[i] - pplA[i])
