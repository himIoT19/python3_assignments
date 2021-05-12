# Program to check given number is perfect or not
# Note: In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

n = int(input("Enter any number: "))
output_sum = 0

# Iterate to find divisors and sum the divisors
for i in range(1, n):
    if n % i == 0:
        output_sum = output_sum + i

# Condition for perfect number
if output_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
