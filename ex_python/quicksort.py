def quicksort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)


temp = [1,2,3,5,2,3,1,5,392,29]
print(quicksort(temp))