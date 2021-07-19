# 愚直に貯金額を足していってn円を超えたら止める
n = int(input())
day = 0
amount = 0
while True:
    day += 1
    amount +=day
    if amount >= n:
        print(day)
        exit()