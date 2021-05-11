# Program to remove the duplicate elements from the list

def remove(list_1):
    """
    Remove the duplicate elements from the list
    :param list_1:
    :return: None
    """
    unique = []
    for item in list_1:
        if item not in unique:
            unique.append(item)
    print(f"length of new list: {len(unique)}")
    return unique


# Driver Code
duplicate = ["delhi", 1, 2, 'a', 3, 3, "Delhi", 3, 3, 4, 5, 'a', "Delhi"]
print(f"length of previous list: {len(duplicate)}")

# Function call
print(remove(duplicate))
