n = int(input())
l = list(map(int,input().split()))
l.sort()
a = 1
mod = 10 ** 9 + 7

for i in range(n):
    if l[i] < i+1:
        print(0)
        exit()
    else:
        a *= l[i]-i
        a %= mod
print(a)