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


H, W = LI()
map = [S() for _ in range(H)]

from typing import List
from pprint import pprint


def rotate(sub_map: List[str]):
    return [line[::-1] for line in sub_map[::-1]]


def mapper(map: List[str]):
    _ = [print(line) for line in map]


out = 0

for shape_h in range(1, H + 1):
    for shape_w in range(1, W + 1):
        for origin_h in range(H - shape_h + 1):
            for origin_w in range(W - shape_w + 1):
                sub_map = [
                    line[origin_w : shape_w + origin_w]
                    for line in map[origin_h : shape_h + origin_h]
                ]
                # print(f"search window: {origin_w=},{origin_h=},{shape_w=},{shape_h=}")
                if sub_map == rotate(sub_map):
                    out += 1
                    # print(f"found one {out}: ----------------")
                    # mapper(sub_map)

print(out)
