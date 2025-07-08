# Big O notation N Logorithmic N 
# best knwon for heap and merge sort algorithms

# an example of a merge sort
# divide: breaking the array into smaaller parts until one sub array have one element
# Conquer: merges the small pieces of the array back together by putting the lowest first resulting in a sorted array

def mergeSort(arr: list[int]):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    leftPart = arr[:middle]
    rightPart = arr[middle:]
    print(leftPart)
    print(rightPart)

    sortedLeft = mergeSort(leftPart)
    sortedRight = mergeSort(rightPart)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i])
    result.extend(right[j])

    return result

unsortedArr = [3, 1, 5, 6, -1, 10, -14, 23.5]
sortedArr = mergeSort(unsortedArr)

print("Sorted array:", sortedArr)
