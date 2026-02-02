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


N, K = LI()
# N, K = [I() for _ in range(N)]
start = N
beans = 0
while True:
    # print(f"{N=} {beans=} {K=}")
    beans += N
    if beans >= K:
        print(N - start)
        break
    N += 1
