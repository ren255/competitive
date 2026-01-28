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


N = I()
L = [I() for _ in range(N)]

volume = 0
play = False
for i in L:
    if i == 1:
        volume += 1
    elif i == 2 and volume >= 1:
        volume -= 1
    elif i == 3:
        play = False if play else True

    if play and volume >= 3:
        print("Yes")
    else:
        print("No")
