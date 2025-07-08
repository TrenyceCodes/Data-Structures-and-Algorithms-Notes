def factorial(n):
    for _ in range(n):
        print(n)
        factorial(n-1)

print(factorial(3))
