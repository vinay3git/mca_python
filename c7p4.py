import csv
filename = "your_data_file.csv"  

with open(filename, 'r') as file:
    data = [line.strip().split(',') for line in file.readlines()]

input_columns = input("Enter column numbers to read (comma-separated, 1-based index): ").split(',')

columns_to_read = [int(i) - 1 for i in input_columns]

for row in data:
    selected_columns = []
    for col in columns_to_read:
        if col < len(row):  
            selected_columns.append(row[col])
        else:
            selected_columns.append(None)  
    
    print(selected_columns)
