def binary_search(values, item):
    low = 0
    high = len(values) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        guess = values[mid]
        
        print(f"before low: {low}, high: {high}, mid: {mid}, guess: {guess}")
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        print(f"after low: {low}, high: {high}, mid: {mid}, guess: {guess}")
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))