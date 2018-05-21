a, b = map(int, input().split(' '))

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

c, d = input().split()
for i in ['+', '-', '*', '//', '%']:
    print(eval(c + i + d))

# 방법은 많다