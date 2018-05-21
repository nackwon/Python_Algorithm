
a, b, c = map(int, input().split())

ex1 = (a + b) % c
ex2 = (a % c + b % c) % c
ex3 = (a * b) % c
ex4 = (a % c * b % c) % c

print(ex1, ex2, ex3, ex4, sep='\n')