#随机快速排序
from random import randint
def QuickSort2(arr):
    
    def partition(arr,l,r):
        if l+1 >= r:return
        a,b=randint(l,r-1),l
        for c in range(l,r):
            if c == a:continue
            if arr[a] >arr[c]:
                b+=1
                arr[b],arr[c] = arr[c],arr[b]
        else:arr[a],arr[b] = arr[b],arr[a]
        partition(arr,l,b)
        partition(arr,b+1,r)
    partition(arr,0,len(arr)) 
    
