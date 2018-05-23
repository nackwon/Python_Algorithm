
number = int(input())

# result = [number * i for i in range(1, 10)]
# print(result)

for i in range(1, 10):
    print("%d * %d = %d" %(number, i, number*i))
