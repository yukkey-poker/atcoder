n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
l.insert(0,[0,0,0])

answer = 'YES'

for i in  range(n):
    t = l[i+1][0]-l[i][0]
    x = l[i+1][1]-l[i][1]
    y = l[i+1][2]-l[i][2]

    move = (t >= abs(x+y))
    parity = ((t % 2) == (x+y) % 2)

    if (move and parity) == True:
        continue
    else:
        answer = 'NO'
        break

print(answer)