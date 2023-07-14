import os
import pandas as pd
from openpyxl import Workbook

def read_sas_datasets(path):
    datasets = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.sas7bdat'):
                dataset_path = os.path.join(root, file)
                datasets.append(dataset_path)

    return datasets

def create_excel_file(datasets, output_file):
    workbook = Workbook()
    worksheet = workbook.active

    for dataset in datasets:
        dataset_name = os.path.basename(dataset)
        df = pd.read_sas(dataset)

        # Write dataset name
        worksheet.append([dataset_name])

        # Write column names
        worksheet.append(list(df.columns))

        # Write column labels
        worksheet.append(list(df.columns.values))

    workbook.save(output_file)
    print("Excel file created:", output_file)

# Example usage
path = '/path/to/datasets'  # Replace with the specific path containing '.sas7bdat' datasets
output_file = '/path/to/output.xlsx'  # Replace with the path of the output Excel file

datasets = read_sas_datasets(path)
create_excel_file(datasets, output_file)
