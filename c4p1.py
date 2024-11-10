def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Number of terms to display
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

print("Fibonacci Series:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")
