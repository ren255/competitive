import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


# N = I()
# A = [LI() for _ in range(N)]

ctn = 0
for char in S():
    if char == "j" or char == "i":
        ctn += 1
print(ctn)
