import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys
import pandas as pd


def I():  # 1行に整数1つ
    return int(sys.stdin.readline().rstrip())


def LI():  # 1行に空白区切りの整数複数
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():  # 1行に文字列1つ
    return sys.stdin.readline().rstrip()


def LS():  # 1行に空白区切りの文字列複数
    return list(sys.stdin.readline().rstrip().split())


from decimal import Decimal, getcontext
import pandas as pd

getcontext().prec = 50

N, T = LI()
# positively,value

data = [LS() for _ in range(N)]
samples = pd.DataFrame(data, columns=["positively", "value"])
samples["positively"] = samples["positively"].apply(Decimal)
samples["value"] = samples["value"].apply(Decimal)
samples["visit"] = Decimal(1)

total_value = Decimal(0)
time = T

while T:
    samples["current_value"] = (samples["value"] / samples["visit"]) * samples[
        "positively"
    ]
    max_id = samples["current_value"].idxmax()
    # print(samples)
    samples.loc[max_id, "visit"] += Decimal(1)
    total_value += samples["current_value"].loc[max_id]
    # print(f"{max_id=}, {T=}, {total_value}(+{samples["current_value"].loc[max_id]})")
    T -= 1

print(total_value)
