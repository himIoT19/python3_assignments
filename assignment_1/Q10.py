# Program to find even numbers from a list of numbers

list_1 = [1, 2, -24, -31, 3, 4, 5, 6, 7, 8, 9, 343, 66, 222, 0]
print(f"List before sorting even numbers: {list_1}")

even_list = []

# Iterate all list elements
for num in list_1:
    if num % 2 == 0:
        even_list.append(num)

print(f"List after sorting even numbers: {even_list}")
