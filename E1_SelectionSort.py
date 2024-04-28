def selectionSort(arr):
    n=len(arr)
    
    for i in range (n-1):
        min=i
        for j in range (i+1,n):
         if arr[j]<arr[min]:
            min=j
            arr[i],arr[min]=arr[min],arr[i]
        
arr=[6,9,4,2,0]
selectionSort(arr)
print(arr)