# Data Cleaning & Preprocessing: Mall Customer Data

## 📝 Project Objective
The main objective of this project is to practice and demonstrate fundamental data cleaning and preprocessing techniques on a raw dataset. By identifying and fixing common data issues, this project aims to prepare the "Mall Customer" dataset for future analysis and modeling.

## 🛠️ Tools
* **Python**: The main programming language used for the data cleaning script.
* **Pandas**: A powerful Python library for data manipulation and analysis.

## 📦 Deliverables
This repository contains the following deliverables:
* **Original Dataset**: `mall-customer.csv` (The raw data with potential issues)
* **Cleaned Dataset**: `cleaned_mall_customer.csv` (The final, processed dataset)
* **Cleaning Script**: `data_cleaning_script.py` (The Python code used to perform the cleaning)
* **Summary of Changes**: A brief overview of the steps taken.

## 🧹 Data Cleaning Summary
The following data cleaning and preprocessing steps were performed on the `mall-customer.csv` dataset:
* **Renaming Columns**: Column headers were standardized to a clean, uniform format (e.g., `Annual Income (k$)` was renamed to `annual_income_k`).
* **Handling Missing Values**: A thorough check was performed, and **no missing values were found** in the dataset.
* **Removing Duplicates**: The dataset was scanned for duplicate rows, and **none were found**.
* **Standardizing Text**: The 'Gender' column was checked for inconsistencies and was already in a consistent format (`Male`, `Female`).
* **Data Type & Format Check**: Data types were verified to ensure they were appropriate for each column (e.g., `age` was an integer). The dataset did not contain any date columns requiring format conversion.

## 🚀 How to Run the Code
You can run the data cleaning script and generate the cleaned dataset yourself by following these steps:
1.  **Clone the Repository**: Clone this repository to your local machine.
2.  **Prerequisites**: Ensure you have Python and the pandas library installed. If not, you can install pandas via pip:
    ```bash
    pip install pandas
    ```
3.  **Run the Script**: Open your terminal or command prompt, navigate to the project folder, and execute the script:
    ```bash
    python data_cleaning_script.py
    ```
The script will print the summary of changes to the terminal and create a new file, `cleaned_mall_customer.csv`, in the same directory.
