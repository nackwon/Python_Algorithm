TestCase = int(input())

for i in range(TestCase):
    count = 0
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:]) / score_list[0]

    for j in score_list[1:]:
        if j > avg:
            count += 1

    result = count / score_list[0] * 100
    print("%0.3f%%" % result)