def quickSort(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quickSort(arr, low, piv - 1)
        quickSort(arr, piv + 1, high)

def partition(arr, low, high):
    piv = arr[low]
    i = low + 1
    j = high
    
    while True:    # continue infinitely until break is reached
        while i <= j and arr[i] <= piv:
            i += 1
        while i <= j and arr[j] >= piv:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j  # returns pivot

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
