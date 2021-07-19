n = int(input())
l = list(map(int,input().split()))
kinomi = 0
for i in range(n):
    if l[i] > 10:
        kinomi += l[i]-10

print(kinomi)