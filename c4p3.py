def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 2  # Starting from the first prime number

    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

# Input the position of the prime number to find
n = int(input("Enter the position of the prime number to find: "))
print(f"The {n}th prime number is:", nth_prime(n))
