# referencing the book "Grokking Algorithms" by Aditya Bhargava chapter 3

# scenario
"""
Suppose you’re digging through your grandma’s attic and come across a mysterious 
locked suitcase. Grandma tells you that the key for the suitcase is probably in 
this other box. his box contains more boxes, with more boxes inside those boxes. 
The key is in a box somewhere. What’s your algorithm to search for the key
"""


# loop algorithm (O(n)) --- IGNORE ---
"""
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through() # Make a pile of boxes to look through.
    while pile is not empty:
        box = pile.grab_a_box() # Grab a box, and look through it.
        for item in box:
            if item.is_a_box():
                pile.append(item) # If you find a box, add it to the pile to look through later.
            elif item.is_a_key():
                print("found the key!") # If you ind a key, you’re done!
"""

# recursve algorithm (O(n)) --- IGNORE ---
"""
def look_for_key(box):
    for item in box: # Look through the box.
        if item.is_a_box():
            look_for_key(item) # If you ind a box, go to step 1.
        elif item.is_a_key():
            print("found the key!") # If you ind a key, you’re done!
"""

# when writing recursive code there's base case and recursive case
"""
def countdown(i):
    print(i)
    if i <= 0: # Base case: base case is the condition under which the recursion stops
        return
    else: # Recursive case: the recursive case is the condition under which the function calls itself
        countdown(i-1)
"""

# call stack: if you forgot what it is, it's probably best to read the book since it's pretty hard to explain here

# but here's a simple call stack with recursion code:
def fact(x):
    factorial = x - 1
    if x == 1:
        return 1
    else:
        return x * fact(factorial)
# call stack: fact(5) -> 5 * fact(4) -> 5 * 4 * fact(3) -> 5 * 4 * 3 * fact(2) -> 5 * 4 * 3 * 2 * fact(1) -> 5 * 4 * 3 * 2 * 1 -> 120
# the program first will call fact(5), because x != 1, it will call fact(5-1) which is fact(4)
# the program will keep calling fact(x-1) until x == 1, at which point it will return 1 and the program will start returning the values back up the call stack
# at this point all fact(5), fact(4) and so on until fact(1) still running and waiting for the return value of fact(1) which is 1
# fact(2) will return 2 * 1 = 2, fact(3) will return 3 * 2 = 6, fact(4) will return 4 * 6 = 24, and finally fact(5) 
# so it will return fact(1) = 1, fact(2) = 2 * 1, fact(3) = 3 * 2, fact(4) = 4 * 6, and finally fact(5) = 5 * 24 
# then the program returns the value and stop
print(fact(5)) # 120