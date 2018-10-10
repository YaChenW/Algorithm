# 选择排序
def selectionSort(arr):
    if len(arr) < 1:
        return arr

    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        change = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = change
    return arr
