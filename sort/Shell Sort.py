#希尔排序
def shellSort(arr):
    n = len(arr)
    if n<2:
        return arr
    h = 1
    while h<n/3:h = h*3+1
    while h>=1:
        for i in range(h,n,h):
            minNum = arr[i]
            for j in range( i-h,-1,-h ):
                if arr[j]>minNum:
                    arr[j+h] = arr[j]
                else:
                    arr[j+h]=minNum
                    break;
            else: arr[j] = minNum
        h //= 3   