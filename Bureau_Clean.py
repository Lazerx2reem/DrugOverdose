

import pandas as pd

# Load the Excel file
file_path="/Users/devanshigupta/Downloads/ACSDP5Y2023.DP05-2025-01-26T223955.xlsx"
data = pd.ExcelFile(file_path)

# Parse the "Data" sheet
data_sheet = data.parse("Data")

# Clean the dataset: Remove metadata rows and set proper column headers
data_cleaned = data_sheet.iloc[2:].reset_index(drop=True)

# Set the first row as the header
data_cleaned.columns = data_cleaned.iloc[0]
data_cleaned = data_cleaned[1:]

# Rename columns for clarity
data_cleaned.columns = ["Label", "Estimate", "Margin_of_Error", "Percent", "Percent_Margin_of_Error"]

# Save the cleaned data to a CSV file
data_cleaned.to_csv("cleaned_socioeconomic_data.csv", index=False)

print("Cleaned data saved as 'cleaned_socioeconomic_data.csv'")

