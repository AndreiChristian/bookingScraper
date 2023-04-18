import csv

def write_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)
    print(f"{len(data)} rows written to {file_path}")

data = [
    ['Name', 'Age', 'Gender'],
    ['John', '30', 'Male'],
    ['Jane', '25', 'Female'],
    ['Bob', '40', 'Male'],
]

write_csv_file('example.csv', data)
