# Python program to find the maximum number among the three numbers

def maximum(a: int, b: int, c: int) -> int:
    if (a >= b) and (a >= c):
        return a  # TODO: Do not use python inbuilt-keywords

    elif (b >= a) and (b >= c):
        return b
    return c


# Driven code
num_1 = 10
num_2 = 14
num_3 = 12

# Function call
print(f"The maximum number is: {maximum(a=num_1, b=num_2, c=num_3)}")
