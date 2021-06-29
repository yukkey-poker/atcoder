n = int(input())
l = sorted(list(map(int, input().split())),reverse=True)

Alice = 0
Bob = 0

if n % 2 ==0:
    for i in range(int(n/2)):
        Alice += l.pop(0)
        Bob += l.pop(0)
else:
    for i in range(int(n//2) + 1):
        Alice += l.pop(0)
        if not l == []:
            Bob += l.pop(0)
        else:
            pass


print(Alice-Bob)
