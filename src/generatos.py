def generador_fibonacci(n):
    a,b = 0,1
    while n > 0:
        yield a
        a, b = b, a+b
        n -= 1

for num in generador_fibonacci(10):
    print(num)