MOD = 998244353

S = input()
l = len(S)

ctn = 0
dp = 0  # s[i]で終わる条件を満たす部分文字列の個数

for i in range(l):
    if i == 0 or S[i] == S[i - 1]:
        dp = 1  # S[i]単体のみ
    else:
        dp = dp + 1  # 前の全部分文字列を延長 + S[i]単体

    ctn = (ctn + dp) % MOD

print(ctn)
