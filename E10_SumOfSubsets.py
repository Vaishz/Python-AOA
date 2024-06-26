def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    
    # Check if the partial sum is equal to target
    if s == target:
        print("Subset Found:", partial)
    
    # If the partial sum exceeds the target or all elements are considered
    if s >= target or not numbers:
        return False
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

# Example usage
numbers = [2, 4, 6, 8, 10]
target = 10
subset_sum(numbers, target)

