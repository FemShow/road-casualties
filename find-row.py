import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/femisokoya/Documents/GitHub/road-casualties/examp_text2.csv')

# Check for missing values in each row
missing_rows = df.isnull().any(axis=1)

# Get the rows with missing values
rows_with_missing_values = df[missing_rows]

# Optional: Count the number of missing values in each row
missing_value_counts = rows_with_missing_values.isnull().sum(axis=1)

# Print a sample of rows with missing values
sample_rows = rows_with_missing_values.head(70)  # Change the number 10 to the desired sample size
print("Sample of rows with missing values:")
print(sample_rows)

# Optional: Print the count of missing values in each row for the sample
sample_missing_value_counts = missing_value_counts.head(10)  # Change the number 10 to the desired sample size
print("\nCount of missing values in each row for the sample:")
print(sample_missing_value_counts)
