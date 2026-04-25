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

F = LI()


if len(set(F)) == len(F):
    print("Yes")
else:
    print("No")


mapping = {}

for m in range(1, M + 1):
    mapping[m] = 0

# print(mapping)

for f in F:
    mapping[f] += 1

# print(mapping)


if 0 not in mapping.values():
    print("Yes")
else:
    print("No")
