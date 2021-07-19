# 制約にAi<=Nとあるので、重複を調べればいい。
n = int(input())
l = list(map(int,input().split()))
l_len = len(l)
s_len = len(set(l))
if l_len == s_len:
    print('Yes')

else:
    print('No')