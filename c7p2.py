# File names
source_file = "source.txt"  # Replace with your source file name
destination_file = "destination.txt"  # Replace with your destination file name

# Open the source file in read mode and destination file in write mode
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    # Loop through each line in the source file
    lines = src.readlines()
    
    # Write odd lines (index 0, 2, 4, ...) to the destination file
    for i in range(len(lines)):
        if i % 2 == 0:  # Odd lines (1st, 3rd, 5th, ...) have even indices (0-based)
            dest.write(lines[i])

print("Odd lines have been copied to", destination_file)
