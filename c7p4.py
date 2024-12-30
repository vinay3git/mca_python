import csv

# File name
csv_file = "data.csv"  # Replace with your CSV file name

# Columns to be read (assuming column indices, 0-based)
columns_to_read = [0, 2]  # Example: Read the 1st and 3rd columns

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Print the content of the specified columns
        selected_columns = [row[i] for i in columns_to_read]
        print(selected_columns)
