n = int(input('Enter a number greater than 1:'))
i = 0

while n!=1:
    if n%2 == 0:
        n /= 2
        i = i+1
    else:
        n = n*3 + 1
        i = i+1

print('Number of steps:',i)
