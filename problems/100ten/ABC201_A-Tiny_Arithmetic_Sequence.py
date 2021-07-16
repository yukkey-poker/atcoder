l = list(map(int,input().split()))
l_std = sorted(l)
if l_std[2]-l_std[1] == l_std[1]-l_std[0]:
    print('Yes')
else:
    print('No')