# common logarithm use base 10
# in this example we will use binary logarithm (base 2) for analyzing algorithms

def binarySearch(values, item):
    low = 0
    high = len(values) - 1
    
    # binary search algorithm (log2(n) or O(log n))
    while low <= high:
        mid = (low + high) // 2
        guess = values[mid]
        
        print(f"before low: {low}, high: {high}, mid: {mid}, guess: {guess}")
        if guess == item:
            print(f"found item: {item} at index: {mid}")
            return mid
        if guess > item:
            high = mid - 1
            print(f"guess: {guess} is greater than item: {item}, setting high to mid - 1: {high}")
        else:
            low = mid + 1
            print(f"guess: {guess} is less than item: {item}, setting low to mid + 1: {low}")
        print(f"after low: {low}, high: {high}, mid: {mid}, guess: {guess}")
    return None

def simpleSearch(values, item):
    low = 0
    high = len(values) - 1
    
    # simple linear search algorithm (n or O(n))
    while low <= high:
        head = low
        guess = values[head]
            
        print(f"before low: {low}, high: {high}, head: {head}, guess: {guess}")
        if guess == item:
                return head
        else:
            low += 1
        print(f"after low: {low}, high: {high}, head: {head}, guess: {guess}")
    return None
    

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(binarySearch(my_list, 3))
print(binarySearch(my_list, -1))
print(simpleSearch(my_list, 16))