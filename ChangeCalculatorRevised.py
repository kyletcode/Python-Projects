def calculate_coins(price):
    # Define the coin values in cents
    coin_values = [25, 10, 5, 1]
    coin_names = ["quarters", "dimes", "nickels", "pennies"]
    
    # Convert price to cents
    remaining_cents = int(price * 100)
    
    # List to hold the count of each coin
    coin_counts = []
    
    # Calculate the amount of each coin
    for value in coin_values:
        count = remaining_cents // value
        coin_counts.append(count)
        remaining_cents %= value
    
    # Print the results
    for name, count in zip(coin_names, coin_counts):
        print(f"{count} {name}")

# Example usage
price = 1.91
calculate_coins(price)
