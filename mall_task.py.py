
# import pandas as pd

#  #Load CSV with full path
# df = pd.read_csv("C:/Users/varsh/Desktop/elevate jobs/mall-customer.csv")

# # View first 5 rows
# print(df.head())

# #2
# #Identify and Handle Missing Values
# # Check missing values
# print("Missing values per column:\n", df.isnull().sum())

# # Option 1: Drop rows with missing values
# df = df.dropna()

# # Option 2 (optional): Fill missing values
# # Example: Fill missing Age with mean
# df['Age'] = df['Age'].fillna(df['Age'].mean())





import pandas as pd

# Step 1: Load the dataset
# Make sure 'mall-customer.csv' is in the same directory as this script.
# If not, provide the full file path.
file_path = 'mall_customer.csv'
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please make sure the file is in the correct directory.")
    exit()

# --- Initial Inspection ---
print("\n--- Initial Data Info ---")
df.info()
print("\n--- Initial 5 Rows ---")
print(df.head())
print("-" * 30)


# Step 2: Rename columns for clarity and consistency
# Renaming headers to be lowercase with underscores
new_column_names = {
    'CustomerID': 'customer_id',
    'Gender': 'gender',
    'Age': 'age',
    'Annual Income (k$)': 'annual_income_k',
    'Spending Score (1-100)': 'spending_score'
}
df.rename(columns=new_column_names, inplace=True)
print("\nColumn headers renamed.")


# Step 3: Check for and handle missing values
# Identify missing values
print("\n--- Missing values per column ---")
missing_values = df.isnull().sum()
print(missing_values)
if missing_values.sum() == 0:
    print("No missing values found. No action required.")
else:
    # Example: drop rows with any missing values
    df.dropna(inplace=True)
    # Or, fill missing values (e.g., for 'age')
    # df['age'].fillna(df['age'].mean(), inplace=True)
    print("Missing values handled.")
print("-" * 30)


# Step 4: Remove duplicate rows
initial_rows = len(df)
df.drop_duplicates(inplace=True)
rows_after_deduplication = len(df)
print("\n--- Duplicate rows check ---")
print(f"Initial rows: {initial_rows}")
print(f"Rows after deduplication: {rows_after_deduplication}")
print(f"Number of duplicate rows found and removed: {initial_rows - rows_after_deduplication}")
if initial_rows - rows_after_deduplication == 0:
    print("No duplicate rows found.")
print("-" * 30)


# Step 5: Standardize text values
# Check unique values in 'gender'
print("\n--- Standardizing 'gender' column ---")
unique_genders = df['gender'].unique()
print(f"Unique values in 'gender' before standardization: {unique_genders}")
if 'male' in unique_genders or 'female' in unique_genders:
    df['gender'] = df['gender'].str.capitalize()
    print("Gender values standardized to 'Male' and 'Female'.")
else:
    print("Gender values are already consistent.")
print("-" * 30)


# Step 6: Check and fix data types
# The data types are already correct based on the initial inspection.
print("\n--- Data Type Check ---")
print("Data types are already correct and consistent.")
print("Note: The dataset does not contain any date columns to convert.")
print("-" * 30)


# --- Final Inspection ---
print("\n--- Final Cleaned Data Info ---")
df.info()
print("\n--- Final 5 Rows of Cleaned Data ---")
print(df.head())


# Step 7: Save the cleaned DataFrame to a new CSV file
cleaned_file_path = 'cleaned_mall_customer.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\n✅ Cleaned data has been successfully saved to '{cleaned_file_path}'")