#三路快排
from random import randint
def QuickSort3Way(arr):
    
    def partition(arr,l,r):
        if l >= r:return
        lt,gt,i,index = l+1,r,l+1,randint(l,r)
        arr[index],arr[l] = arr[l],arr[index]
        while i <= gt:
            if arr[i]>arr[l]:
                arr[i],arr[gt] = arr[gt],arr[i]
                gt-=1
            elif arr[i]<arr[l]:
                arr[i],arr[lt] = arr[lt],arr[i]
                lt+=1
                i+=1
            else:i+=1
        arr[l],arr[lt-1] = arr[lt-1],arr[l]
        partition(arr,l,lt-1)
        partition(arr,gt+1,r)
    partition( arr,0,len(arr)-1 )
