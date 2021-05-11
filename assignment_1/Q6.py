# check the number is in given range

def check_range(n: int):
    """
    Function to find whether the number is present in the provide range
    :param n:
    :return:
    """
    if n in range(10, 20):
        print(f"Number {n} is in the range.")
    else:
        print("The number is not in given range.")


# Function call
check_range(15)
