import csv

input_file = 'feat_eng1.csv'
output_file = 'feat_eng2.csv'

# Define the column headings to copy
columns_to_copy = ['LSOA Code', 'LSOA Name', 'Year', 'Fatal', 'Serious']

# Read the input CSV file and perform the specified actions
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    writer = csv.writer(file_out)
    reader = csv.reader(file_in)

    # Get the indices of the columns to copy
    header_row = next(reader)
    column_indices = [i for i, header in enumerate(header_row) if header.strip() in columns_to_copy]

    # Write the header row with modified column headings
    updated_header_row = ['LSOA Code', 'LSOA Name', 'Year', 'Severity', 'Casualty Numbers']
    writer.writerow(updated_header_row)

    # Process the remaining rows
    for row in reader:
        # Filter non-blank columns and modify the values accordingly
        updated_row = [row[i] if i in column_indices else '' for i in range(len(row))]
        updated_row[3] = updated_row[3] if updated_row[3] else '0'
        updated_row[4] = updated_row[4] if updated_row[4] else '0'

        # Write the updated row to the file
        writer.writerow(updated_row)

print("Column cloning completed. The result is saved in feat_eng2.csv.")
