import pandas as pd

# Load the Excel file
input_file = 'data/input.xlsx'
output_file = 'output/filtered_age_output.xlsx'

# Read the data from Sheet1
df = pd.read_excel(input_file, sheet_name='Sheet1')

# Filter for age > 18
filtered_df = df[df['age'] > 18]

# Save the filtered data to a new Excel file
filtered_df.to_excel(output_file, index=False)
