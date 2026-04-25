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
A = LI()

from collections import defaultdict

hash_table = defaultdict(list)
for i, value in enumerate(A):
    hash_table[value].append(i)

vale_ctn = defaultdict(int)
for i, value in enumerate(A):
    vale_ctn[value] += 1

vale_ctn = vale_ctn.items()
# print(vale_ctn)
vale_ctn = [(item[0], item[0] * item[1]) for item in vale_ctn]
vale_ctn = sorted(vale_ctn, key=lambda x: x[1])[::-1]

sorted_unique = [item[0] for item in vale_ctn]
# print(vale_ctn, sorted_unique)

for x in sorted_unique[:K]:
    for i in hash_table[x]:
        A[i] = 0
    # print(f"removed {x} index:{hash_table[x]}")
    # print(A)


print(sum(A))
