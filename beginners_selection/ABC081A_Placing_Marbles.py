s = str(input())
answer = 0
for i in range(3):
    if s[i] == '1':
        answer += 1
    else:
        answer = answer

print(answer)