# Big o notation of n squared N^2
# the input size of n grows on a quadratic time complexity

# an good example of this could be a nested for loop checking for duplicates


def has_Duplicates(nums: list[int]) -> bool:
    # we initialize two for loops with variables i and j
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # we check for the duplicates
            if nums[i] == nums[j]:
                return True

    return False


print(has_Duplicates([1, 2, 3, 4, 6, 8, 1]))
