import csv

# File name
csv_file = "data.csv"  # Replace with your CSV file name

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Print the list of strings (row) for each line
        print(row)
