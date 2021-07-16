import math
p = int(input())
n=10
count=0
while n > 0:
    fact = math.factorial(n)
    count += p // fact
    p %= fact
    n -=1

print(count)