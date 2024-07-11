# First Way to Sort a list
numbers = [8, 3, 9, 3, 5, 1]

sortedList = sorted(numbers)

print("Sorted List: ", sortedList)


# Second Way to Sort a list
numbers = [8, 3, 9, 3, 5, 1]

# Length of the list
n = len(numbers) # n = 6

# Bubble Sort Algorithm
for i in range(n): # i = 6
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Print the sorted list
print("Sorted list:", numbers)