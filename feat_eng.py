import csv

input_file = '/Users/femisokoya/Documents/GitHub/road-casualties/examp_text2.csv'
output_file = 'feat_eng1.csv'

# Read the input CSV file and perform the specified actions
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    writer = csv.writer(file_out)
    reader = csv.reader(file_in)

    # Write the header row to the output file
    header_row = next(reader)
    writer.writerow(header_row[:3] + [header_row[3], header_row[4], header_row[5], header_row[6]])

    # Process the remaining rows
    for row in reader:
        output_rows = []
        output_rows.append(row[:3] + [header_row[3], row[3]])
        output_rows.append(row[:3] + [header_row[4], row[4]])
        output_rows.append(row[:3] + [header_row[5], row[5]])
        output_rows.append(row[:3] + [header_row[6], row[6]])

        # Write the output rows to the file
        writer.writerows(output_rows)

print("Column manipulation completed. The result is saved in feat_eng1.csv.")