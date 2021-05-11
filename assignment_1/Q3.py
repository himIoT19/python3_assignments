# multiply all the elements in the list

total = 1
# creating a list
list_1 = [8, 2, 3, -1, 7]

# Iterating for all the list indices
for item in list_1:
    if item.__class__.__name__ in ["int", "float"]:
        total = total * item

print(f"The multiplication of list_1 elements is equal to: {total}")
