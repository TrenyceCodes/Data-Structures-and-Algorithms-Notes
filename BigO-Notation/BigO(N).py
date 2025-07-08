# Big O notation of n 
# known as a linear time complexity since the input size n grows linearly

def findElement(target: int, nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

print(findElement(target=5, nums=[1,2,3,4,5]))

def AddItemsInArray(nums: list[int]) -> int:
    total = 0
    for i in range(len(nums)):
        total += nums[i]

    return total

print(AddItemsInArray(nums=[1,2,3,4,5]))


nums=[1,2,3,4,5]
for i in range(len(nums)):
    print(nums[i])
