# Big O of Logorithmic n, also known for splitting the input size by 2
# the input size grows on a logarithmic time complexity
def BinarySearch(target: int, nums: list[int]) -> int:
    #low is the first number in the array
    #high is the last number in the array
    #these are considered two pointers
    low = 0
    high = len(nums)-1

    while low <= high:
        #handles splitting the array in half,
        #choosing a number
        middle = low +(high-low)//2
        print(middle)

        if nums[middle] == target:
            #returns middle index that target is found
            return middle 
        elif nums[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1

if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7]
    target = 1

    result = BinarySearch(target=target, nums=nums)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
