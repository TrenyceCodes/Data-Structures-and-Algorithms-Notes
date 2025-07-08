# Big O N! - factorial time
# this grows factorial time complexity

def factorial(n: int):
    for _ in range(n):
        print(n)
        factorial(n-1)

print(factorial(3))

