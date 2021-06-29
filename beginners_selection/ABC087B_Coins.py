# 500円玉A枚、100円玉B枚、50円玉C枚から何枚か選び、
# X円ちょうどにする組み合わせの数
a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

if (0 <= a,b,c <= 50) and (a+b+c >= 1) and (50 <= x <= 20000) and (x % 50 == 0):
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 500*i + 100*j + 50*k ==x:
                    count += 1
else:
    print('エラー：入力値の範囲を確認してください')

print(count)
