
str1 = input()

result = '\n'.join(str1[i:i+10] for i in range(0, len(str1), 10))

print(result)