sugar = int(input())
count = 0
while sugar % 5 != 0:
    if sugar < 0:
        count = -1
        break
    sugar -= 3
    count += 1
count += sugar // 5
print(count)
