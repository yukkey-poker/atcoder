n,x=map(int,input().split())
l = list(map(int,input().split()))
for i in range(n):
    if i % 2 == 1:
        l[i] -= 1
    else:
        pass

if sum(l) <= x:
    print('Yes')

else:
    print('No')