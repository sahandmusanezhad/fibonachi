def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b

for n in fibonacci(20):
    print(n)