# The filter in python will help us to filter the list.
# The filter faction take two arguments: the first is the lambda function as an anonymous function, and the second argument is the list of numbers.
# Syntax: filter(function, list)
# When we call the filter function, it iterates over the provided list and passes every value one by one to the function, which returns true or false.
# If that particular value's result is true, it gets added to the list. the classic example of lambda functions with the filter() method is to filter out the even and odd numbers from the list of numbers

# list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# one liner code to make the list of even numbers use filter() function

even_no = list(filter((lambda x: x % 2 == 0), numbers))

# even number list
print(even_no)