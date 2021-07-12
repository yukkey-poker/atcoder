# 入力の受け取り
n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
# 入力例
# 4
# 3 8 5 1
# ↓
# n = 4
# l = [8, 5, 3, 1]
# 条件分岐
if l[0] < sum(l[1:]):
# リストlの０番目が、リストlの１番目以降すべての合計値より小さいなら「YES」を出力。
# 8 < (5+3+1)
# 8 < 9 → YES
    print('YES')

else:
    print('NO')