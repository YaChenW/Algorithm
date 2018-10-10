#快排
def quickSort(arr):
    if len(arr)<2:
        return arr
    arr1,arr2 = [],[]
    flag = arr[len(arr)//2]
    for i in range(0,len(arr)):
        if arr[i]>flag:
            arr2.append(arr[i])
        elif arr[i]<flag:
            arr1.append(arr[i])
    ret = quickSort(arr1)
    ret.append(flag)
    ret.extend(quickSort(arr2))
    return ret