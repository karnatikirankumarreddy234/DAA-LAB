def min_max(arr):
    if(len(arr)==1):
        return arr[0],arr[0]
    M=len(arr)//2
    left=arr[:M]
    right=arr[M:]
    l_min,l_max=min_max(left)
    r_min,r_max=min_max(right)
    
    return min(l_min,r_max),max(l_max,r_max)

arr = [10, 50, -5, 20, 30]
print("Correct:", min_max(arr)) 
