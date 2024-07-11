# Write a program that calculates profit margin and prints how much a item/service should be sold for profit.

def calculate_profit_margin(x):
    profit_margin = x
    diff_profit_margin = 100 - profit_margin
    return diff_profit_margin

def calculate_sell_price(a, b):
    item_cost = a
    profit_margin1 = b
    sell_price = item_cost / profit_margin1
    return sell_price


item_cost = int(input("How much is the item/service you trying to sell?: "))
item_cost = item_cost * 100
print(item_cost)

profit_margin1 = int(input("Enter a profit margin: "))
profit_margin1 = calculate_profit_margin(profit_margin1)
print(calculate_profit_margin(profit_margin1))

sell_price = calculate_sell_price(item_cost, profit_margin1)
print("Item sell price is: {:.2f}".format(sell_price))



