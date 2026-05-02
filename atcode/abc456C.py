MOD = 998244353

S = input()
l = len(S)

ctn = 0
dp = 0

for i in range(l):
    if i == 0 or S[i] == S[i - 1]:
        dp = 1
    else:
        dp = dp + 1

    ctn = (ctn + dp) % MOD

print(ctn)
