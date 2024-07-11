# Psuedo Code:
# What I want the program to do:

# 1: Welcome the user to the store / DONE
# 2: Ask user what products they would like to buy / DONE
# 3: Display price next to product / DONE
# 4: Asks users the amount/quantity of product they would like to buy / DONE
# 5: Ask user if they would like checkout or not
# 6: During checkout display products, quantity, and total price.



#/ #1: Welcome the user to the store
name = input(str("What is your name: "))
print("Hello " + name + ", welcome to Rancher's Food Market")

# 2: Ask user what products they would like to buy
# products = ["1. pizza", "2. hamburger", "3. hotdog", "4. spaghetti", "5. pudding"]
# print("What products would you like to buy?")
# print(*products, sep = "\n") # Separates list indexes with a new line after index

products2 = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
food = []
quantity = []
option = 0
totalprice = 0

while option == 0:
    print("\n")
    print("1. Pizza       $5.39\n2. Hambuger    $3.49\n3. Hot Dog     $2.69\n4. Spaghetti   $4.29\n5. Pudding     $2.49\n")

    productChoice = int(input("What food would you like to buy?: "))
    if productChoice == 1:
        food.append("Pizza")
        count = int(input("How many do you want? "))
        quantity.append(count)
        totalprice = totalprice + count * float(5.39)
    elif productChoice == 2: 
        food.append("Hamburger")
        count = int(input("How many do you want? "))
        quantity.append(count)
        totalprice = totalprice + count * float(3.49)
    elif productChoice == 3:
        food.append("Hotdog")
        count = int(input("How many do you want? "))
        quantity.append(count)
        totalprice = totalprice + count * float(2.69)
    elif productChoice == 4:
        food.append("Spaghetti")
        count = int(input("How many do you want? "))
        quantity.append(count)
        totalprice = totalprice + count * float(4.29)
    elif productChoice == 5:
        food.append("Pudding")
        count = int(input("How many do you want? "))
        quantity.append(count)
        totalprice = totalprice + count * float(2.49)
    elif productChoice == 6:
        print("")
        print("Heres is what you want to buy: \n")
        print("Total Price: $", float(totalprice))
        length = len(food)
        for i in range (length):
            print(food[i], quantity[i])
    elif productChoice == 0:
        exit()

# Make a list of 
# def productCount(buying, count):