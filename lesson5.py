# Write a function that takes an unknown number of arguments and returns their sum.
def adittion(*numbers):
    sum = 0
    for number in numbers:
        sum +=number
        return sum
numbers = (38.493,90,30)    
print(adittion(numbers))




# Write a function that takes two arguments, the first being a string and the second
# being an unknown number of integers. The function should return a new string where
# # the integers have been added to the original string.
def multiple_numbers(str, *numb):
    word = str
    for n in numb:
        word +=str(n)
        return word

print (multiple_numb("I was born in" 2001))

# Write a function that takes an unknown number of keyword arguments and returns
# a dictionary where the keys are the argument names and the values are the argument values.
def unkown (*kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print(unkown(name= "Linda ", age= 28))

# Write a function that takes a function and an unknown number of arguments,
# and returns the result of calling the function with the arguments.
def unkown_number(function, *args):
    result =   function(*args)
    return result
print (10,10)

# Write a function that takes a list of integers and an unknown number of
# keyword arguments. The function should return a new list where each integer
# in the original list has been multiplied by the value of the corresponding keyword argument.


# Write a function that takes a list of integers and an unknown number
# of additional integers as arguments. The function should return the
# index of the first occurrence of the sum of the list and the additional integers


# Write a function that takes an unknown number of keyword arguments,
# each with a string value. The function should concatenate all the
#  strings and return the resulting string.: