# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop()
        return popped * multiply_list(l)
       

# Return the factorial of n
def factorial(n):
    if n ==1:
        return 1
    else:
        return factorial(n-1) * n
    

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    else:
        return count_list(l[1:])+1

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop()
        return popped + sum_list(l)


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:
        popped = l.pop()
        return [popped] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return None
    elif l[0] == i:
        return i
    else:
        rest = l[1:]
        return find(rest, i)

# Determines if a string is a palindrome
def palindrome(some_string):
    listed = list(some_string)
    if len(listed) <= 1:
        return True
    elif listed[0] == listed[-1]:
        listed.pop()
        (reverse(listed)).pop()
        return palindrome("".join(listed)) 
    else:
        return False

# Given the width and height of a sheet of paper,
 # and the number of times to fold it, return the final dimensions of the sheet as a tuple. 
 # Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    if width > height:   
        return fold_paper(float(width/2) , height, folds - 1)
    else:
        return fold_paper(width, float(height/2), folds - 1)
    

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if target == n:
        print target
    else:
        print n
        count_up(target, n+1)



# Test functions
# l = [2, 3, 4,]
# some_string = "SEES"
#print factorial(5)
#print multiply_list(l)
# print sum_list(l)
# print count_list(l)
# print fibonacci(10)
# print find(l, 6)
# print palindrome(some_string)
# print fold_paper(20.4, 12.4, 0)
count_up(7, 5)