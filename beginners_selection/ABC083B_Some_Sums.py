n,a,b = map(int, input().split())

if (1 <= n <= 10000) and (1 <= a,b <= 36):
    some_sum = 0
    l = [i for i in range(n+1)]

    while (n+1) > 0:
        num = l.pop(0)
        some_num = sum(list(map(int, str(num))))

        if a <= some_num <= b:
            some_sum += num
            n -= 1
        else:
            n -= 1

print(some_sum)
