# The Python map() function is mostly used to modify the items in the list.

# It takes two arguments, the first argument is the lambda function as an anonymous function, and the second argument is the list.

# Syntax : map( function, list)

# The map() function iterates over the list provided as a parameter and each value is passed as a parameter to evaluate with the expression of the lambda function. Then these evaluated values get returned one after another.

# Suppose we want to create a list of squares of numbers from the given list of numbers.

# given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_numbers = list(map((lambda x: x*x), numbers))

print(sq_numbers)
