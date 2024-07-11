def multiply(x, y): #X and y are placeholder and will accept integers variables due to * sign
    product = x * y
    return product #When doing any sort of math within functions always use return to return value back to the call.

def add(x, y): #X and y are placeholder and will accept integers variables due to + sign
    add = x + y
    return add

def subtract(x, y): #X and y are placeholder and will accept integers from both multiply and add functions to combine to subtract
    sub = x - y
    return sub

product = multiply(5, 8)
print(product)

print()

addition = add(5, 8)
print(addition)

print()

subtraction = subtract(product, addition)
print(subtraction)



