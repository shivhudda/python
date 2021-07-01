# built-in function
a=10
b=34
c = sum((a,b))
print(c)

# user-defined function
def function1(a,b):
    return a+b
print(function1(10,34))

# using docstring
def function2(a,b):
    """
    this function returns average of a and b.
    this function does not work for three digits.
    """
    average = (a+b)/2
    return average
print(function2(22,25))
# print a docstring
print(function2.__doc__)