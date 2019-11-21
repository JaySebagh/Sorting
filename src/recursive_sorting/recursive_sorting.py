# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    newArr = []
    start = 0
    startA = 0
    startB = 0

    while startA + startB < elements:
        # print(startA, startB)
        if startB >= len(arrB):
            newArr.extend(arrA[startA:])
            startA += 1
            break
        elif startA >= len(arrA):
            newArr.extend(arrB[startB:])
            startB += 1
            break
        elif arrB[startB] < arrA[startA]:
            newArr.append(arrB[startB])
            startB += 1
        else:
            newArr.append(arrA[startA])
            startA +=1
    return newArr

# merge([0, 3, 4, 5, 8], [1, 2, 6, 7, 9])

# [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def merge_sort( arr ):
    if len(arr) == 1:
        return arr
    mid_point = len(arr) // 2
    result_left = merge_sort(arr[:mid_point])
    result_right = merge_sort(arr[mid_point:])
    solution = merge(result_left, result_right)
    return solution

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3]))

# (len(arr)% 2) == 0 --> even