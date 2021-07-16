n,k=map(int,input().split())
l = list(map(int,input().split()))
std_l = sorted(l)
dic = {}
okashi = k//n
k_dash = k%n
for i in range(n-1):
    dic[std_l[i]]=okashi

if k_dash > 0:
    for j in range(k_dash):
        dic[std_l[j]] = okashi+1

for k in range(n-1):
    print(dic[l[k]])