import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/femisokoya/Documents/GitHub/road-casualties/examp_text2.csv')

# Define the row numbers you want to send
row_numbers = [4835, 9672, 14509, 19346, 19355, 19367, 19373, 19386, 19388, 19393]  # Update with the desired row numbers

# Extract the rows with specified row numbers
selected_rows = df[df.index.isin(row_numbers)]

# Send the contents of selected rows
for index, row in selected_rows.iterrows():
    # Access the values of each column in the row
    column1_value = row['LSOA Code']
    column2_value = row['LSOA Name']
    column2_value = row['Year']
    column2_value = row['Fatal']
    column2_value = row['Serious']
    column2_value = row['Slight']
    column2_value = row['Annual Casualties']
    # Add more columns as needed
    
    # Send the values or perform any desired action
    print(f"Row {index}: Column1={column1_value}, Column2={column2_value}")
