'''List comprehensions provide a concise way to create lists. 

    My Notes: 
    A list comprehension is a compact, readable way to create a new list 
    from an existing iterable (like a list, range, or string) using a single line of code.

    BASIC SYNTAX: [expression for item in iterable]

    It consists of brackets containing an expression followed by a for clause, then
    zero or more for or if clauses. The expressions can be anything, meaning you can
    put in all kinds of objects in lists.

    The result will be a new list resulting from evaluating the expression in the
    context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
    new_list = []
    for i in original_list:
        if filter(i):
            new_list.append(expressions(i))  

    # You can obtain the same thing using list comprehension:
    # newer more efficient way shown below. Older way shown above

    new_list = [expression(i) for i in original_list if filter(i)]
'''

#The list comprehension starts with a '[' and ']', to help you remember that the
# result is going to be a list.

'''
#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter/conidtion*     ]

'''

# 1st example of list comprehension
list1 = list(range(1,11))
list2 = []

for x in list1:
    if x > 5:
        x *= 20
        list2.append(x)

print(list2)

# 2nd example of list comprehension but more concise
list2 = [x * 20 for x in list1 if x > 5]

print(list2)



squares = [x**2 for x in range(1,11)]
print(squares)

list1 = [3,4,5]

multiplied = [item*3 for item in list1]
print(multiplied)


# Example with words
listOfwords = ["this","is","a","list","of","words"]
items =[word[0] for word in listOfwords]
print(items)

# Example with upper/lower
upper = [x.upper() for x in ["a","b","c"]]
print(upper)

lower = [x.lower() for x in upper]
print(lower)


new_range = [i*i for i in range(10) if i % 2 == 0 ]
print(new_range)

# Faster way to print numbers from "Hello 12345 World"
    # is.digit() function returns just integers
string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)

# The normal way to print just the numbers in "Hello 12345 World"
numbers = []
for x in string: 
    if x.isdigit():
        numbers.append(int(x))

print(numbers)

# Extracting from test.txt file 

infile = open("test.txt", "r")
result = [i.rstrip('\n') for i in infile if "line3" in i ]
print(result)


def double(x):
    return x*2

print(double(10))


doublelist = [double(x) for x in range(10) if x % 2 == 1]
print(doublelist)


newlist = [x + y for x in [10,30,50] for y in [20,40,60]]
print(newlist)

#The filter part answers the question if the item should be transformed.



## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

#numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]




## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

# dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
# "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}




## Find all the numbers from 1 to 1000 that have a 4 in them



## count how many times the word 'the' appears in the text file - 'sometext.txt'



## Extract the numbers from the following phrase ##

# phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each " +
# "event, with about 3 or 4 that were classifled as serious per event.'






