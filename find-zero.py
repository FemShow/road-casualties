import pandas as pd

# Read the CSV file
df = pd.read_csv('examp_text2.csv')

# Iterate over each column
for column in df.columns:
    # Check if the column contains numeric values
    if df[column].dtype == 'object':
        # Convert values that are 'o' or 'O' to 0
        df[column] = pd.to_numeric(df[column].replace(['o', 'O'], '0'), errors='coerce')

# Save the modified DataFrame back to the CSV file
df.to_csv('examp_text2.csv', index=False)
