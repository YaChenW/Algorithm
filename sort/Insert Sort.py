# 插入排序,数组的越有序,速度越块,对完全有序数组排序,时间复杂度为O(n)
def insertSort(arr):
    if len(arr) <= 1:return arr

    for i in range(0, len(arr)-1):
        for j in range(i, -1, -1):
            if arr[j] < arr[j + 1]:
                break
            arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
