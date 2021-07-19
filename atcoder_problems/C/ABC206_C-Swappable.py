n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
d = {}
key_l = []
for i in range(n):
    if l[i] not in d:
        d[l[i]] = 1
        key_l.append(l[i])
    else:
        d[l[i]] += 1
ans = 0
for j in key_l:
    ans += (n - d[j])*d[j]

print(int(ans/2))