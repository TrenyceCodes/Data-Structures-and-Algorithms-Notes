# Big O of One or O(1) - represents the time it takes is constant and not dependent on the input of a function

#Examples
x = 5 + (15 * 20)
print(x)

def addUp(n: int) -> float:
    total = n * (n+1)/2
    return total

print(addUp(2))

array1 = [1, 2, 3, 4, 5]
print(array1[1])
array1.insert(1, 1)

def get_first_element(arr: list[int]) -> int:
    return arr[0]

print(get_first_element(array1))

def check_positive(n: int) -> bool:
    if n > 0:
        return True
    return False

print(check_positive(-1))

def max_of_two(a: int, b: int):
    if a > b:
        return a
    return b

print(max_of_two(a=1, b=3))

def complex_conditions(a: int, b: int, c: int) -> bool:
    if a > 10 and b < 5 or c == 0:
        return True
    return False

print(complex_conditions(a=1, b=3, c=4))

# this happens when the if statement contributes to complexity
nums = [4, 5, 6, 7, 7]
def count_odds(arr: list[int]):
    count = 0
    for num in arr:
        if num % 2 == 1:
            count += 1
    return count

nums.append(4)
nums.pop()

