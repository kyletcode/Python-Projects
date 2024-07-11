def multiply(x, y): #X and y are placeholder and will accept integers variables due to * sign
    product = x * y
    return product #When doing any sort of math within functions always use return to return value back to the call.

def add(x, y): #X and y are placeholder and will accept integers variables due to + sign
    add = x + y
    return add

def subtract(x, y): #X and y are placeholder and will accept integers from both multiply and add functions to combine to subtract
    sub = x - y
    return sub

num1 = int(input("Whats first number you want to multiply?: "))
num2 = int(input("Whats second number you want to multiply?: "))

add_num = add(num1, num2) #Adds the inputs
print(add_num)
print()

sub_num = subtract(num1, num2) #Subtracts the inputs
print(sub_num)
print()

multiply_num = multiply(num1, num2) #Multiply the inputs
print(multiply_num)

