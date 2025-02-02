2import pandas as pd

# Step 1: Load the pre-downloaded CSV file
file_path = "/Users/devanshigupta/Documents/CODE/cleaned_socioeconomic_data.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Step 2: Filter and process the data as needed
# For example, selecting columns of interest
df = df[['NAME', 'B19013_001E', 'B17001_002E', 'DP02_0066PE']]
df.columns = ['County', 'Median_Household_Income', 'Poverty_Count', 'HS_Grad_Percent']

# Step 3: Save the processed data
df.to_csv("socioeconomic_data_processed.csv", index=False)
print("Socioeconomic data processed and saved successfully!")
