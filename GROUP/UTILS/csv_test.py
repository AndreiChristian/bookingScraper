import csv

def write_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)
    print(f"{len(data)} rows written to {file_path}")

