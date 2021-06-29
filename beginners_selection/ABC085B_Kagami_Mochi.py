n=int(input())
d_list = []
for i in range(n):
    l = int(input())
    if l:
        d_list.append(l)

d_set = set(d_list)

print(len(d_set))