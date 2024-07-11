def check_number(x, y):
    answer = x % y
    return answer #returns value back to answer variable

input = int(input("What number do you want to divide?: "))
answer = check_number(input, 2) #passing in input as x within function, same goes for 2

if answer == 0:
    print("You have an even number")
    print(answer)
else:
    print("You have an odd number")
    print(answer)