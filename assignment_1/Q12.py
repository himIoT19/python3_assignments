# Program to find the string is a palindrome string

def is_palindrome(str_1: str) -> bool:
    """
    Function to find the string is a palindrome string
    :param str_1: String
    :return: boolean True/False
    """
    if str_1 == str_1[::-1]:
        return True
    return False


# Driver code
s = "madam or nurses run"
# s = 'madam'

# Function call and save the result returned by the function call
ans = is_palindrome(s)

if ans:
    print("Yes, the string is a palindrome string")
else:
    print("No, the string is not a palindrome string")
