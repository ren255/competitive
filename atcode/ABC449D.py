import bisect, collections, copy, heapq, itertools, math, string
import numpy as np
import sys


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


L, R, D, U = LI()


def is_black(x, y=0):
    return max(abs(x), abs(y)) % 2 == 0


# L≤x≤R かつ D≤y≤U

corners = []
edges = []
ctn = 0

Xs = list(range(L, R + 1))
Ys = list(range(D, U + 1))
print("x:", Xs)
print("y:", Ys)

edge_x = []
for x in Xs:
    if is_black(x, Ys[0]):
        edges.append([x, Ys[0]])
        edge_x.append(x)
    if is_black(x, Ys[-1]):
        edges.append([x, Ys[-1]])
        edge_x.append(x)
edge_x = set(list(edge_x))

edge_y = []
for y in Ys:
    if is_black(y, Xs[0]):
        edges.append([Xs[0], y])
        edge_y.append(y)
    if is_black(y, Ys[-1]):
        edges.append([Xs[-1], y])
        edge_y.append(y)

edge_y = set(list(edge_y))

for y in edge_y:
    for x in edge_x:
        if abs(x) == abs(y) and is_black(x, y):
            corners.append([x, y])

for x, y in edges:
    if (x == Xs[0] or x == Xs[0]) or (y == Ys[0] or y == Ys[0]):
        corners.append([x, y])
corners = list({tuple(p) for p in corners})

for corner in corners:
    

# corners = list(set(corners))
print(ctn, edges)

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

for points, color, label in [(edges, "blue", "edges"), (corners, "red", "corners")]:
    xs, ys = zip(*points)
    plt.scatter(xs, ys, color=color, zorder=5, label=label)
    for x, y in points:
        plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(8, 4))

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Points")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
