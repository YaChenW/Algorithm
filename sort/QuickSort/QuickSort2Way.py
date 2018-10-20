#双路快排
from random import randint
def QuickSort2Way(arr):
    
    def partition(arr,l,r):
        if l >= r:return
        index,i,j = randint(l,r),l+1,r
        arr[index],arr[l] = arr[l],arr[index]
        while True:
            while arr[i]<=arr[l] and i<r: i+=1
            while arr[j]>=arr[l] and j>l: j-=1
            if i>=j:
                arr[l],arr[j] = arr[j],arr[l]
                break
            else:arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        partition( arr,l,j-1 )
        partition( arr,j+1,r )
    partition( arr,0,len(arr)-1 )    
