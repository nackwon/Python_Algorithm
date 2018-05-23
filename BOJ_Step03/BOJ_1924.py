a, b = map(int, input().split(" "))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
str1 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(str1[(sum(days[:a-1])+b-1) % 7])

