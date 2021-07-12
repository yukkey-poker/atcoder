n,y = list(map(int, input().split()))
y = int(y/1000)
for i in range(n+1):
    for j in range(n-i):
        k = n -(i + j)
        if 10*i + 5*i + k == y:
            print(i, j, k)
            exit()

print(-1, -1, -1)