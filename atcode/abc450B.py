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
C = [LI() for _ in range(N - 1)]

# 1≤a<b<c≤N
# 0<=a<b<=N-1

found = False


def get_price(a, b):
    x = a - 1
    y = b - a - 1
    return C[x][y]


for a in range(1, N - 1):
    # print(f"{a=}")
    for b in range(a + 1, N):
        # print(f"{b=}")
        for c in range(b + 1, N + 1):
            # print(f"{c=}")
            # print(
            #     f"condition{a},{b},{c}.is:{get_price(a, c) > get_price(a, b) + get_price(b, c)}"
            # )
            if get_price(a, c) > get_price(a, b) + get_price(b, c):
                found = True
                break

if found:
    print("Yes")
else:
    print("No")
