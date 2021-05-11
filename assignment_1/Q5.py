# factorial of a number

def fact(n: int) -> int:
    """
    Function used to get factorial
    :param n:
    :return:
    """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


number = 5
output = fact(number)
if output == 0:
    print("The entered number to find factorial is negative")
else:
    print(f"Factorial of {number} is: {output}")
