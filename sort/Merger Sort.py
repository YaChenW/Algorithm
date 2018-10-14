#当数据较小时，代码数量影响较大，插入排序比归并更快
#使用更少的空间
#归并排序
def mergeSort5(arr):
    def insertSort(arr,l,r):
        for i in range(1,r-l+1):
            minNum = arr[i+l]
            for j in range(i-1,-1,-1):
                if minNum < arr[j+l]:
                    arr[j+l+1] = arr[j+l]
                else: 
                    arr[j+l+1] = minNum
                    break
            else: arr[j+l] = minNum
    
    def toMergeSort(arr,l,r):
        if (r-l)<15:
            insertSort(arr,l,r)
            return
        mid = l + (r-l)//2
        toMergeSort(arr,l,mid)
        toMergeSort(arr,mid+1,r)
        index1,index2,size1,size2 = l,mid+1,mid+1,r+1
        if arr[mid]<arr[mid+1]:return
        aux = arr[l:r+1]
        i = l
        while index1 < size1 or index2 < size2:
            if index1 == size1 or (index2<size2 and aux[index1-l] > aux[index2-l]) :
                arr[i]=aux[index2-l]
                index2+=1
            else:
                arr[i]=aux[index1-l]
                index1+=1
            i+=1
            
    toMergeSort(arr,0,len(arr)-1)


