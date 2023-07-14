import os
import struct
import csv
from openpyxl import Workbook

def read_sas_dataset(path):
    dataset = {
        'name': os.path.basename(path),
        'columns': [],
        'labels': []
    }

    with open(path, 'rb') as f:
        f.read(56)  # Skip the header section

        while True:
            chunk = f.read(4)
            if chunk == b'':  # End of file
                break

            length = struct.unpack('I', chunk)[0]
            chunk = f.read(length)

            if chunk.startswith(b'HEADER'):
                # Skip the header information
                continue
            elif chunk.startswith(b'COLUMN'):
                column_info = chunk[8:].decode('utf-8').split('\x00')
                column_name = column_info[0]
                column_label = column_info[1]

                dataset['columns'].append(column_name)
                dataset['labels'].append(column_label)

    return dataset

def create_excel_file(datasets, output_file):
    workbook = Workbook()
    worksheet = workbook.active

    for dataset in datasets:
        # Write dataset name
        worksheet.append([dataset['name']])

        # Write column names
        worksheet.append(dataset['columns'])

        # Write column labels
        worksheet.append(dataset['labels'])

    workbook.save(output_file)
    print("Excel file created:", output_file)

# Example usage
path = '/path/to/datasets'  # Replace with the specific path containing '.sas7bdat' datasets
output_file = '/path/to/output.xlsx'  # Replace with the path of the output Excel file

datasets = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.sas7bdat'):
            dataset_path = os.path.join(root, file)
            dataset = read_sas_dataset(dataset_path)
            datasets.append(dataset)

create_excel_file(datasets, output_file)
