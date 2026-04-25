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
stock_list = [LI() for _ in range(M)]


from collections import defaultdict

trade_map = defaultdict(list)
for u, v in stock_list:
    trade_map[u].append(v)

print(trade_map)

from collections import deque
