# Open the file in read mode
file_name = "example.txt"  # Replace with your file name
lines = []

# Open the file
file = open(file_name, 'r')

# Read each line and store it in the list
lines = file.readlines()

# Close the file
file.close()

# Print the list containing all lines
print(lines)
