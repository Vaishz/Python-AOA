def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        l_half=arr[:mid]
        r_half=arr[mid:]
        l_half_sorted=merge_sort(l_half)
        r_half_sorted=merge_sort(r_half)
        return merge(l_half_sorted,r_half_sorted)
    
def merge(left,right):
    new=[]
    i,j=0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
            
    new.extend(left[i:])    #adds all remaining elements which didn't come in the loop
    new.extend(right[j:])
    return new

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
            
    