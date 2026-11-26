# loop
def loopSum(arr):
    arr = arr.copy()
    total = 0
    for i in range(len(arr)):
        total += arr.pop(0)
    return total

# recursive
def recurSum(arr):
    arr = arr.copy()
    total = 0
    if len(arr) == 0:
        return total
    else:
        total += arr.pop(0)
        return total + recurSum(arr)
    
def recurCountItems(arr):
    arr = arr.copy()
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        return 1 + recurCountItems(arr)
    
def recurBinSearch(arr, item, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1  # not found

    mid = (low + high) // 2

    if arr[mid] == item:
        return mid
    elif item < arr[mid]:
        return recurBinSearch(arr, item, low, mid - 1)
    else:
        return recurBinSearch(arr, item, mid + 1, high)
    
# calling function
def sum(arr, condition):
    if condition == "loop":
        return loopSum(arr)
    else:
        return recurSum(arr)
    
def countitems(arr, condition):
    if condition == "loop":
        return len(arr)
    else:
        return recurCountItems(arr)

array = [1, 2, 3, 4, 5]

print(sum(array, "loop"))
print(sum(array, "else"))
print(countitems(array, "recursive"))
print(recurBinSearch(array, 4))