# Program to check the number is prime or not

def prime(num):
    """
    Function used to check the number is prime or not
    :param num: int
    :return: none
    """
    if num > 1:
        is_prime = True
        for i in range(2, int(num / 2) + 1):

            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(f"The {num} is prime number.")
        else:
            print(f"The {num} is not prime number.")

    else:
        print(num, "is not a prime number")


# Function call
prime(373)
