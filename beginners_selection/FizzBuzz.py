n= int(input())
text = 'FizzBuzz'

if n % 15 == 0:
    print(text)
elif n%5 == 0:
    print(text[:4])
elif n%3 == 0:
    print(text[4:])
else:
    print(n)