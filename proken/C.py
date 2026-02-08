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
log = [LS() for _ in range(N)]

flor = 1
under_ground = 0
# 地下1階 = 0 とする

for step in log:
    C, D = step[0], int(step[1])
    if C == "U":
        flor += D
    elif C == "D":
        flor -= D
    if flor <= 0:
        under_ground += 1

print(under_ground)
