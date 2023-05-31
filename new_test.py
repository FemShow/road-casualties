import csv

# Define the input and output file paths
input_file = '/Users/femisokoya/Documents/GitHub/road-casualties/examp_text2.csv'
output_file = 'new_file.csv'

# Define the column headers
new_column_headers = ['LSOA Code', 'LSOA Name', 'Year', 'Severity', 'Casualty Number']

# Read the input CSV file and copy the required columns to the output file
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    # Write the new column headers to the output file
    writer.writerow(new_column_headers)

    # Read the first row (original column headers) and find the indices of the required columns
    first_row = next(reader)
    required_columns = ['LSOA Code', 'LSOA Name', 'Year', 'Fatal', 'Serious', 'Slight']
    column_indices = [first_row.index(column) for column in required_columns]

    # Iterate over the remaining rows and write the required columns to the output file
    for row in reader:
        lsoa_code = row[column_indices[0]]
        lsoa_name = row[column_indices[1]]
        year = row[column_indices[2]]
        severity = ['Fatal', 'Serious', 'Slight']
        casualties = [int(row[idx]) for idx in column_indices[3:6]]
        annual_casualties = sum(casualties)

        # Write the row with the required columns to the output file
        writer.writerow([lsoa_code, lsoa_name, year, severity, casualties, annual_casualties])

print("Column manipulation completed. The result is saved in new_test_file.csv.")
