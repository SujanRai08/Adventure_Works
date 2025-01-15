def parition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            (arr[i],arr[j]) = (arr[j],arr[i])
        (arr[i+1],arr[high]) = (arr[high],arr[i+1])
        return i

def quick_sort(arr,low,high):
    if low<high:
        pi = parition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quick_sort(data,0,size-1)
print('sorted array in ascending order: ')
print(data)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))  # Output: [1, 5, 7, 8, 9, 10]
