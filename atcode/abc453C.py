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


from time import time

N = I()
L = LI()

pos = 0.5
pass_zero = 0

start = time()

for move in L:
    # print(f"pos:{pos}  move:{move} diff:{abs(pos - 0)}")
    if abs(pos - 0) < move:
        pass_zero += 1
        # print("pass")

    if 0 < pos:
        pos -= move
    else:
        pos += move

duration = time() - start
print(f"duration:{duration:.5f}, max_time:{(duration/N)*10**9:.2f}")


print(pass_zero)
