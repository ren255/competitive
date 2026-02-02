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
map = [[0 for _ in range(N)] for _ in range(N)]

from pprint import pprint


r, c = 0, (N - 1) // 2
map[r][c] = 1
k = 1

for _ in range(N**2 - 1):
    r1, c1 = (r - 1) % N, (c + 1) % N
    if map[r1][c1] == 0:
        map[r1][c1] = k + 1
        r, c = r1, c1
        # print(f"({r1},{c1}) is 0. writing {k +1}")
    else:
        r, c = (r + 1) % N, c
        map[r][c] = k + 1
        # print(f"({r1},{c1}) is not 0. writing {k+1} to ({r},{c})")

    k += 1

for row in map:
    for i in range(len(row)):
        print(row[i], end="")
        if i != len(row) - 1:
            print(" ", end="")

    print()
