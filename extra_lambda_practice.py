# USING A LAMBDA FUNCTION
remainder = lambda num: num % 2
print(remainder(5))
print("-"*20)



# USING A (CLOSURE) LAMBDA FUNCTION WITH DEFINING A FUNCTION 
def testfunc(num):
    print(num)
    return lambda x:x * num 

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))
print("-"*20)



# USING A (CLOSURE) LAMBDA FUNCTION WITH DEFINING A FUNCTION (EASIER WAY)
result10 = lambda x: x * 10 
result100 = lambda x: x * 100
print(result10(9))
print(result100(9))
print("-"*20)




# OLD WAY FOR USING filter() FUNCTION THAT COULD USE LAMBDA
    # filter(function,iterable)
    # 
numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

def filtered(x):
    if x > 7: 
        return x

filtered_list = list(filter(filtered, numbers_list))
print(filtered_list)
print("-"*20)

# MORE EFFICIENT WAY USING LAMBDA WITH filter() FUNCTION
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)
print("-"*20)




# USING LAMBDA WITH map() FUNCTION
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)







