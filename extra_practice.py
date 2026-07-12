# USING FOR LOOP
list1 = list(range(1,11))
list2 = []

for x in list1:
    if x > 5:
        x *= 20
        list2.append(x)
print(list2)


# USING LIST COMPRENSION
list2 = [x*20 for x in list1 if x>5]
print(list2)




# USING LIST COMPRENSION WITH A RANGE
squares = [x**2 for x in range(1,11)]
print(squares)


# USING LIST COMPRENSION WITH A LIST
list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)



# USING LIST COMPRENSION WITH A LIST OF WORDS
listOfwords = ["this","is","a","list","of","words"]
items =[word[0] for word in listOfwords]
print(items)


# USING LIST COMPREHENSION WITH UPPER/LOWER
upper = [x.upper() for x in ["a","b","c"]]
print(upper)

lower = [x.lower() for x in upper]
print(lower)




# USING LIST COMPREHENSION USING GENERAL FORM 
# new_range = [ expression          iterable        filter/condition ]
new_range = [i*i for i in range(10) if i % 2 == 0 ]
print(new_range)



# USING LIST COMPREHENSION USING STRING AND IS.DIGITS FUNCTION
# Faster way to print numbers from "Hello 12345 World"
    # is.digit() function returns just integers
string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)



# USING LIST COMPREHENSION TO EXTRACT INFO FROM  test.txt FILE
infile = open("test.txt", "r")
result = [i.rstrip('\n') for i in infile if "line3" in i ]
print(result)


# DEFINING A FUNCTION AND CALLING FUNCTION 
def double(x):
    return x*2
print(double(10))
# PASSING A LIST COMPREHENSION 
doublelist = [double(x) for x in range(10) if x % 2 == 1]
print(doublelist)



# NESTED LIST COMPREHENSION 
newlist = [x + y for x in [10,30,50] for y in [20,40,60]]
print(newlist)

