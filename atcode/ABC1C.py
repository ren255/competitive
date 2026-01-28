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
L = [LI() for _ in range(M)]

# 各研究者の利害関係者数をカウント
conflict_count = {i: 0 for i in range(1, N + 1)}

for m1, m2 in L:
    conflict_count[m1] += 1
    conflict_count[m2] += 1

# 各研究者について査読者の組み合わせを計算
for i in range(1, N + 1):
    # 査読者候補の人数 = 全体 - 著者本人 - 利害関係者
    candidates = N - 1 - conflict_count[i]

    # 候補者から3人を選ぶ組み合わせ nC3 = n*(n-1)*(n-2)/6
    if candidates >= 3:
        combinations = candidates * (candidates - 1) * (candidates - 2) // 6
    else:
        combinations = 0

    print(combinations)
