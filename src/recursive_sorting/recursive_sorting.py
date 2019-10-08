# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    newArr = []
    start = 0
    startA = 0
    startB = 0

    while startA + startB < elements:
        print(startA, startB)
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
# [1, 2, 4, 5, 8] [0, 3, 6, 7, 9]
def merge_sort( arr ):
    
    return arr