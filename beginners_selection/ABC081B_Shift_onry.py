n = int(input())
num_list = list(map(int,input().split()))

count = 0

if n < 201:
    while True and n:
        x = all(i % 2 == 0 for i in num_list) #True or False
        if x == True:
            num_list = [i/2 for i in num_list]
        else:
            break
        count += 1
        num_list = num_list
    
    print(count)