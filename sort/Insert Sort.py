# 插入排序,数组的越有序,速度越块,对完全有序数组排序,时间复杂度为O(n)
def insertSort(arr):
    if len(arr) < 1:
        return arr

    for i in range(1, len(arr)):
        minNum = arr[i]
        for j in range(i, 0, -1):
            if minNum < arr[j - 1]:
                arr[j] = arr[j - 1]
            else:
                arr[j] = minNum
                break
        else:
            arr[j - 1] = minNum
    return arr