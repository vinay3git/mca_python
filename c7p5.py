import csv

def write_dict_to_csv(file_path, data_dict):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data_dict.keys())
        writer.writeheader()
        writer.writerow(data_dict)

def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def get_user_input():
    data_dict = {}
    while True:
        key = input("Enter the field name (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter the value for {key}: ")
        data_dict[key] = value
    return data_dict

file_path = "sample.csv"

user_dict = get_user_input()

write_dict_to_csv(file_path, user_dict)

print("\nCSV file content:")
read_csv(file_path)
