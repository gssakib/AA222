def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [for x in arr if x == pivot]
    right = [for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    print(quicksort([3,6,8,10,1,2,1]))

main()