# reverse string
def reverse(a_str: str) -> str:
    """
    Function used for reversing the string
    :param a_str: String
    :return: String
    """
    string_1 = a_str[::-1]
    return string_1


# String to work on
s = "I love python"

print("Old string : {}".format(s))
print(f"New string after reversal: {reverse(s)}")
