number = int(input())

for i in range(number, 0, -1):
    print(i)

m = map(str, range(int(input()), 0, -1))
print(type(m))
print('\n'.join(m))