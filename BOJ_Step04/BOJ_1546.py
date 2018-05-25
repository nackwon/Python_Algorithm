first_number = int(input())
changeData = first_number
count = 0
while True:
    first = changeData // 10
    second = changeData % 10
    count += 1

    changeData = (second * 10) + ((first + second) % 10)

    if first_number == changeData:
        break
print(count)
