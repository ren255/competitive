import bisect, collections, copy, heapq, itertools, math, string
import sys


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


# H 行 W 列のブロックからなる長方形状のチョコレートがあります。
H, W, Q = LI()
querry = [LI() for _ in range(Q)]

for T, V in querry:

    if T == 1:
        H -= V
        ate = W * V
    elif T == 2:
        W -= V
        ate = H * V

    print(ate)
