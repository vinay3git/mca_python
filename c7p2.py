# File names
source_file = "source.txt"  # Replace with your source file name
destination_file = "destination.txt"  # Replace with your destination file name

# Open the source file in read mode and destination file in write mode
src = open(source_file, 'r')
dest = open(destination_file, 'w')

# Loop through each line in the source file, keeping track of line number
line_number = 1
for line in src:
    if line_number % 2 != 0:  # If the line number is odd
        dest.write(line)
    line_number += 1

# Close both files
src.close()
dest.close()

print("Odd lines have been copied to", destination_file)
