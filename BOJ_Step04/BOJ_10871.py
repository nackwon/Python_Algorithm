a, b = map(int, input().split(' '))
list = input().split(' ')

for i in list:
    if b > int(i):
        print(i, sep=' ')