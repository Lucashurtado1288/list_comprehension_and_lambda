# 1st example of list comprehension
list1 = list(range(1,11))
list2 = []

for x in list1:
    if x > 5:
        x *= 20
        list2.append(x)

print(list2)


# 2nd example of list comprehension but more concise, same result as example 1
list2 = [x * 20 for x in list1 if x > 5]

print(list2)

# 2nd example cont. print squares of range using LC, list comprehension
    # **2, is treated as exponent or to the power of ^2
    # result is a list of squares in range of 1-11
    # range is a start and stop function, meaning 11 is the number it will stop at 
squares = [x**2 for x in range(1,11)]
print(squares)


# 2nd Example cont. 
    # LC will mutiply each item by 3 for item in list
    # multipled variable is then used like a function when printing
list1 = [3,4,5]

multiplied = [item*3 for item in list1]
print(multiplied)

# Example with words
    # printing the first letter in each word
listOfwords = ["this","is","a","list","of","words"]
items =[word[0] for word in listOfwords]
print(items)

# Example with upper/lower
    # changing items in list to uppercase letters
upper = [x.upper() for x in ["a","b","c"]]
print(upper)

lower = [x.lower() for x in upper]
print(lower)

# Using LC, to square each number i from 0-9 only if i is even

    # if i % 2 == 0 , this only keeps even numbers 
        # 0,2,4,6,8
    # expression i*i
        # now each remaining value is squared: 
        # 0^2 = 0 
        # 2^2 = 4 
        # 4^2 = 16 
        # 6^2 = 36 
        # 8^2 = 64 

new_range = [i*i for i in range(10) if i % 2 == 0 ]
print(new_range)



## Exercise ##

# Example 1: Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
    # which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = [int(x) for x in numbers if x > 0]
print(newlist)



## Example 2: create a list of integers which specify the length of each word in
    ## a sentence except for the word 'the'
    ## != , means to exclude "the" word
    ## sentence.split(), is a string method that breaks a sentence into a list of words
        # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

lengths = [len(word) for word in words if word != "the"]
print(lengths)



## Example 3: 
    ## Given dictionary is consisted of vehicles and their weights in kilograms. 
    ## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
    ## In the same list comprehension make the key names all upper case.
        # dict.items() → gives (key, value) pairs
        # for vehicle, weight in ... → unpack key and value

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

vehicles_below_5000_kilograms = [vehicle.upper() for vehicle, weight in dict.items() if weight < 5000]
print(vehicles_below_5000_kilograms)


## Example 4: 
    ## ## Find all the numbers from 1 to 1000 that have a 4 in them

numbers_with_four = [i for i in range(1,1001) if '4' in str(i)]
print(numbers_with_four)



## Example 5: 
    ## count how many times the word 'the' appears in the text file - 'sometext.txt'
    ## result equals 27

infile = open("sometext.txt", "r")

result = len([word for word in infile.read().lower().split() if word == "the"])
print(result)
infile.close()


## Extract the numbers from the following phrase ##

phrase = ('In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each ' +
'event, with about 3 or 4 that were classifled as serious per event.')


numbers_from_sentence = [int(word) for word in phrase.split() if word.isdigit()]
print(numbers_from_sentence)