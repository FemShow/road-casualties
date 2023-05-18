import pandas as pd

# Read the data into a DataFrame
# df = pd.read_csv('examp_text.txt', sep='\t')

df = pd.read_excel('/Users/femisokoya/Documents/GitHub/road_length/road-casualties/example1.xlsx', sheet_name='LSOA11')


# Initialize a new DataFrame to store the extracted values
extracted_df = pd.DataFrame(columns=['LSOA Code', 'LSOA Name', 'Year', 'Fatal', 'Serious', 'Slight', 'Annual Total'])

# Define the sets of columns to extract
column_sets = [[0, 1, 7, 8, 9, 10, 11], 
               [0, 1, 12, 13, 14, 15, 16], 
               [0, 1, 17, 18, 19, 20, 21], 
               [0, 1, 22, 23, 24, 25, 26], 
               [0, 1, 27, 28, 29, 30, 31], 
               [0, 1, 32, 33, 34, 35, 36], 
               [0, 1, 37, 38, 39, 40, 41], 
               [0, 1, 42, 43, 44, 45, 46]]

# Define the corresponding column labels
column_labels = ['LSOA Code', 'LSOA Name', 'Year', 'Fatal', 'Serious', 'Slight', 'Annual Total']

# Loop through the column sets and extract the values
for columns in column_sets:
    extracted_values = df.iloc[:, columns].values
    extracted_df = pd.concat([extracted_df, pd.DataFrame(extracted_values, columns=column_labels)], ignore_index=True)

# Save the extracted DataFrame to a CSV file
extracted_df.to_csv('examp_text2.csv', index=False)
