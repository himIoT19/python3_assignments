# sum all the elements in the list
total = 0

# creating a list
list_1 = [11, 5, 17, 18, 23, 'lemon', "783", 1.0]

# Checking if the list contains the integers/float/other data type
for item in list_1:
    if item.__class__.__name__ in ["int", "float"]:
        total = total + item
    continue

print(f"Sum of all elements in the list is equal to: {total}")
