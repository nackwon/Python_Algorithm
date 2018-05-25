number = int(input())
score = list(map(int, input().split()))

print("%0.2f" %(sum(score)/max(score) * 100 / number))