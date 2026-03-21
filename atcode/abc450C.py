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
MAP = [S() for _ in range(H)]


def is_adjacent(pos1, pos2):
    """2 つのマス(i,j),(i′ ,j′ ) が隣接しているとは、∣i−i′ ∣+∣j−j′ ∣=1 であることと定めます。"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1


from collections import deque


class Pos:
    def __init__(self, x, y):
        self.col = x
        self.row = y

    def __str__(self):
        return MAP[self.row - 1][self.col - 1]

    def is_adjacent(self, pos: Pos):
        """2 つのマス(i,j),(i′ ,j′ ) が隣接しているとは、∣i−i′ ∣+∣j−j′ ∣=1 であることと定めます。"""
        return abs(pos.col - self.col) + abs(pos.row - self.row) == 1

    def is_edge(self):
        if self.col == 1 or self.row == 1 or self.col == W or self.row == H:
            return True
        else:
            return False

    def up(self):
        if self.row - 1 <= 0:
            return None
        return Pos(self.col, self.row - 1)

    def left(self):
        if self.col - 1 <= 0:
            return None
        return Pos(self.col - 1, self.row)

    def right(self):
        if self.col + 1 >= W:
            return None
        return Pos(self.col + 1, self.row)

    def down(self):
        if self.row + 1 >= H:
            return None
        return Pos(self.col, self.row + 1)

    def neighbors(self):
        positions = []
        positions.append(self.down())
        positions.append(self.up())
        positions.append(self.left())
        positions.append(self.right())

        return [p for p in positions if p is not None]

    def get_grupe(self):
        queue = deque(self.neighbors())
        white = [self]
        visited = {self}

        while queue:
            pos = queue.popleft()
            if pos in visited:
                continue
            visited.add(pos)

            if str(pos) == ".":
                white.append(pos)
                queue.extend(pos.neighbors())

        return white

    def __eq__(self, other: Pos):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))


edge_white = set()
in_white = set()
grupe_n = 0

for col in range(1, W + 1):
    for row in range(1, H + 1):
        pos = Pos(col, row)
        if str(pos) == ".":
            if pos.is_edge():
                ps = tuple(pos.get_grupe())
                edge_white.add(ps)
                print(f"found edge white len:{len(ps)}")
            else:
                if pos not in in_white:
                    grupe_n += 1
                ps = tuple(pos.get_grupe())
                in_white.add(ps)
                print(f"found in white len:{len(ps)}. and new:{pos not in in_white}")


print()
print(grupe_n, len(edge_white))
