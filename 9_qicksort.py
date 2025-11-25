def partition(arr,low,high):
    pivot=arr[high]
    pindex=low
    for j in range (low ,high):
        if(arr[j]<=pivot):
            arr[j],arr[pindex]=arr[pindex],arr[j]
            pindex+=1                       
    arr[pindex],arr[high]=arr[high],arr[pindex]
    return pindex
def quicksort(arr,low,high):
    if (low<high):
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
        
arr=[10,7,1,8,9,6,5]
low=0
high=len(arr)-1
quicksort(arr,low,high)
print(arr)
    
    