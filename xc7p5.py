import csv

# Python dictionary
data_dict = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

# File name
csv_file = "output.csv"

# Write dictionary to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header (keys of the dictionary)
    writer.writerow(data_dict.keys())
    
    # Write the rows (values of the dictionary)
    rows = zip(*data_dict.values())  # Transpose the dictionary values to get rows
    writer.writerows(rows)

print("Dictionary written to CSV file.")

# Read the CSV file and display its content
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Print each row
    for row in csv_reader:
        print(row)
