
# Explanation of how lambda function works
    # A lambda function is a small, anonymous (unnamed) function in Python.
    # A lambda function can only contain one expression (no multiple lines, no statements).
        # remainder variable below now acts like a function when lamdba function is called

# 1st Example: 
remainder = lambda num: num % 2

print(remainder(5))

# 1st Example cont.:
    # Same example as above but how it would be coded previously before using lambda
    # prints the same result 1
def remainder(num):
    return num % 2

print(remainder(5))


# 2nd Example
product = lambda x,y: x * y 

print(product(2,3))


# 3rd Example: 

def testfunc(num):
    print(num)
    return lambda x:x * num 

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

# 3rd Example written out a different format, same result

result10 = lambda x: x * 10 
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))

# The filter() Function, the function takes a lambda function together
    # with a list as the arguments

    # Following syntax: filter(object, iterable)

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

def filtered(x):
    if x > 7: 
        return x

filtered_list = list(filter(filtered, numbers_list))
print(filtered_list)


# 1st Example using lambda function with explanation used above
    # will result in the same result as done above
    # alot more efficent and save memory

filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)


# The map() function
    # using the numbers_list as mentioned above in filter() example
    # Basic Syntax:  map(function, iterable)
    # The map() function in Python is used to apply a function to every item in an iterable
        # (like a list, tuple, etc.) and return a new iterable with the results.

mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)
