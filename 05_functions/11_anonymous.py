# An anonymous in python is a function that is defined without a name.
# Unlike functions defined using def keyword>
# These are defined using the lambda keyword and are hence called lambda functions.
# They can have 0 or more arguments but only one return value.

# lambda arguments: expression

square = lambda x : x*x

print(square(4))

def square(x):
    return x*x

print(square(4))