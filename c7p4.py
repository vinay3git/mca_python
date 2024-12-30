import csv

# File name
csv_file = "data.csv"  # Replace with your CSV file name

# Get columns to read from user input (comma-separated, 1-based index)
columns_input = input("Enter column numbers to read (comma-separated, 1-based index): ")

# Convert the user input into a list of integers (1-based index converted to 0-based)
columns_to_read = [int(i) - 1 for i in columns_input.split(',')]

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the specified columns and print them
        selected_columns = [row[i] for i in columns_to_read]
        print(selected_columns)
