#冒泡排序
def bubbleSort( arr ):
    if len(arr)<1:
        return arr
    for i in range(len(arr)):
        flag = True
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = False
        if(flag):break
    return arr
