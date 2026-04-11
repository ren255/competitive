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
shape = [LI() for _ in range(N)]

M = I()
strings = [S() for _ in range(M)]

# print(shape)
# print(strings)

offset = max([bone[1] for bone in shape])

for a, b in shape:
    pad = offset - b
    left = b - 1
    right = a - b
    # print(" " * pad + "." * left + "#" + "." * right)


char_dics = []

for index, letter in enumerate(strings):
    letter_map = {}
    for j, char in enumerate(letter):
        if char not in letter_map.keys():
            letter_map[char] = []
        letter_map[char].append(j)
    char_dics.append(letter_map)


char_length = []

for letter in strings:
    char_length.append(len(letter))


# # from pprint import pprint

# pprint(char_dics)

# for size, letter, letter_map in zip(char_length, strings, char_dics):
# print(f"{letter} len:{size}")
# pprint(letter_map)


for target in strings:
    submit = []
    # print("\n\ntarget is:", target)
    complete = True
    for index, pos in enumerate(shape):
        if len(target) != N:
            # print("target is too smaill")
            complete = False
            continue

        a, b = pos
        # print("serching for:", a, b, target[index])
        candidates = []
        for i, length in enumerate(char_length):
            if length == a:
                candidates.append(i)

        if len(candidates) == 0:
            complete = False
            # print("no letters with", a)
            break

        # print("canditates:", candidates, [strings[can] for can in candidates])

        found = False
        for candidate in candidates:
            if not target[index] in char_dics[candidate].keys():
                # print(strings[candidate], "faild")
                continue
            postions = char_dics[candidate][target[index]]
            if (b - 1) in postions:
                submit.append(strings[candidate])
                # print(strings[candidate], "found")
                found = True
                break
        if not found:
            complete = False
            break

    if complete:
        print("Yes")
    else:
        print("No")

    for letter, pos in zip(submit, shape):
        pad = offset - pos[1]
        # print(" " * pad + letter)
