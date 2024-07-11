import math
#What I want the program to do

# 1. Ask user to input a price
# 2. Grab the price and check if quarters, dimes, nickles, and pennies can be used as change
# 3. Print amount of coins for each that would fulfill the inputed price



def calculateQuarters (price):
    quarterCount = price / .25 # quarterCount = 6
    amount.append(math.floor(quarterCount))
    quarterPrice = .25 * math.floor(quarterCount) # quarterPrice = 1.50
    newPrice = price - quarterPrice # newPrice = 1.57 - 1.50
    return newPrice

def calculateDimes (price): # Start here
    if price >= .10:
        dimeCount = price / .10 
        amount.append(math.floor(dimeCount))
        dimePrice = .10 * math.floor(dimeCount) 
        newPrice = price - dimePrice
        return newPrice
    else:
        amount.append(0)

def calculateNickels (price):
    if price >= .05:
        nickelCount = price / .05 
        amount.append(math.floor(nickelCount))
        nickelPrice = .05 * math.floor(nickelCount)
        newPrice = price - nickelPrice 
        return newPrice
    else:
        amount.append(0)

def calculatePennies (price):
    if price >= .01:
        pennyCount = price / .01 
        amount.append(math.floor(pennyCount))
        pennyPrice = .01 * math.floor(pennyCount)
        newPrice = price - pennyPrice 
        return newPrice
    else:
        amount.append(0)

coins = ["Quarters: ", "Dimes: ", "Nickels: ", "Pennies: "]
amount = []

price = float(input("Enter Price: "))

#print("%.2f" % price)
#print("%.2f" % float(calulateQuarters(price)))
#print("%.2f" % float(calulateDimes(price)))
#print("%.2f" % float(calulateNickels(price)))
#print("%.2f" % float(calculatePennies(price)))

while price != 0:
    if price >= .25:
        price = (calculateQuarters(price))
    elif price >= .10:
        price = (calculateDimes(price))
    elif price >= .05:
        price = (calculateNickels(price))
    elif price >= .01:
        price = (calculatePennies(price))
    else:
        length = len(amount)
        for i in range (length):
            print(coins[i], amount[i])
        print(amount)
        exit()




