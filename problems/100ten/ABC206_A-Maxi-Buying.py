n=int(input())
n_tax = int(n*1.08//1)
if n_tax<206:
    print('Yay!')

elif n_tax>206:
    print(':(')

else:
    print('so-so')