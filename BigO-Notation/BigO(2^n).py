# this is a good example of Big O notation of 2 squared n
# when the input size increases by 1, the number of it operations executed is doubled.
# we can label this as an exponential time complexity
def recursiveFibonnaci(n: int):
    if n < 2:
        return n

    return recursiveFibonnaci(n - 1) + recursiveFibonnaci(n - 2)

print(recursiveFibonnaci(10))
