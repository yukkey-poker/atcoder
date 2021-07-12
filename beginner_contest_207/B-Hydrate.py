a,b,c,d = list(map(int,input().split()))
count=0
blue = a+b*count
red = c*count
old_blue = a+b*(count-1)
old_red = c*(count-1)

while True:
    if blue//d <= red:
        print(count)
        exit()
    else:
        count+=1
        old_blue = blue
        old_red = red
        blue = blue
        red=red

        if old_blue-old_red > blue-red:
            continue
        else:
            print(-1)
            exit()

