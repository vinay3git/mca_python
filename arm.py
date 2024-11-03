# Program to check if a number is an Armstrong number

number = int(input("Enter a number: "))
sum_of_digits = 0
temp = number
num_digits = len(str(number))

# Using a while loop to calculate the sum of the digits raised to the power of num_digits
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** num_digits
    temp //= 10

# Checking if the number is an Armstrong number
if number == sum_of_digits:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
