# Make a program that ask a user to input how much their car is, how many months they have to fully pay off their car, and how much is the monthly payment.
# Then print a list showing all the monthly payments incrementing.

def calculate_down_payment(x, y):
    total = x
    dp = y

    down_payment = dp / 100
    total1 = total * down_payment
    return total1

def calculate_cost(z): #Calculates total cost through cost total, down payment, and monthly payment
    monthly = z

    total_cost = x / monthly
    return total_cost


global x

try:
    cost_total = float(input("What is the price of the car?: "))
    print()

    down_payment = float(input("How much down payment do you want to put on the car? (10-20%): "))
    total = calculate_down_payment(cost_total, down_payment)
    print("Your down payment is: " + str(total))
    print()

    x = cost_total - total
    print("You have to pay a total amount of: " + str(x) + " over the next few months")

    print()
    monthly = int(input("How many months do you want to pay for the car? (12-84): "))
    payment_total = calculate_cost(monthly)
    print("Your total payment per month is: {:.2f}".format(payment_total))

    counter = 0
    payment = 0

    while counter <= monthly - 1:
        payment += payment_total
        counter = counter + 1
        print("Month " + str(counter) + ": {:.2f}".format(payment))

except ValueError as e:
    print(e)
    print("Enter only numbers please")

finally: #Always at the end and will always print towards the end of program
    print("Run the program again but please input the correct values this time, thank you")