n = 5  # Number of rows in the upper half

# Upper half of the pattern using nested loops
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half of the pattern using nested loops
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
