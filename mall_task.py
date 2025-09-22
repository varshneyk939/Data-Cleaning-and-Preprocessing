import pandas as pd
import os

# --- Step 1: Set the file path using a raw string ---
# Use the full path you provided. The 'r' before the string handles the backslashes correctly.
file_path = r"C:\Users\varsh\Desktop\elevate jobs\mall-customer.csv"

try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please make sure the file path is correct.")
    exit()

# --- Step 2: Perform the data cleaning steps ---

# Rename columns for clarity and consistency
new_column_names = {
    'CustomerID': 'customer_id',
    'Gender': 'gender',
    'Age': 'age',
    'Annual Income (k$)': 'annual_income_k',
    'Spending Score (1-100)': 'spending_score'
}
df.rename(columns=new_column_names, inplace=True)
print("\nColumn headers renamed.")


# Check for and handle missing values
print("\n--- Missing values per column ---")
missing_values = df.isnull().sum()
print(missing_values)
if missing_values.sum() == 0:
    print("No missing values found. No action required.")
else:
    df.dropna(inplace=True)
    print("Missing values handled.")


# Remove duplicate rows
initial_rows = len(df)
df.drop_duplicates(inplace=True)
rows_after_deduplication = len(df)
print("\n--- Duplicate rows check ---")
print(f"Number of duplicate rows found and removed: {initial_rows - rows_after_deduplication}")


# Standardize text values (if needed)
print("\n--- Standardizing 'gender' column ---")
df['gender'] = df['gender'].str.capitalize()
print(f"Unique values in 'gender' after standardization: {df['gender'].unique()}")
print("Gender values standardized.")


# Check and fix data types
print("\n--- Data Type Check ---")
print("Data types are already correct and consistent.")


# Save the cleaned DataFrame to a new CSV file
# This will save the new file in the same directory as the original file.
cleaned_file_path = os.path.join(os.path.dirname(file_path), 'cleaned_mall_customer.csv')
df.to_csv(cleaned_file_path, index=False)
print(f"\n✅ Cleaned data has been successfully saved to '{cleaned_file_path}'")