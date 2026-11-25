# sorting from largest to smallest (descending order) using selection sort algorithm
def findLargest(arr):
    if not arr:
        raise ValueError("arr must not be empty")
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

# sorting from smallest to largest (ascending order) using selection sort algorithm
def findSmallest(arr):
    if not arr:
        raise ValueError("arr must not be empty")
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# selection sort algorithm (n^2 or O(n^2)) (generally not efficient for large datasets) (should be written (n * 1/2 * n) but Big O notation ignores constants)
def selectionSort(arr, order):
    arr = arr.copy() # copy the original array to avoid modifying it
    newArr = []
    for i in range(len(arr)):
        if order == "descending":
            largest = findLargest(arr)
            newArr.append(arr.pop(largest))
        else:
            smallest = findSmallest(arr)
            newArr.append(arr.pop(smallest))
    return newArr

unordered_list = [5, 2, 9, 3, 7, 1, 8, 4, 6]

print(selectionSort(unordered_list, "ascending"))
print(selectionSort(unordered_list, "descending"))
