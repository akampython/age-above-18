import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
input_file = 'data/input.xlsx'
output_image = 'output/filtered_age_output.png'

# Read the data from Sheet1
df = pd.read_excel(input_file, sheet_name='Sheet1')

# Filter for age > 18
filtered_df = df[df['age'] > 18]

# Plot age distribution
plt.figure(figsize=(10, 6))
filtered_df['age'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Age Distribution (Above 18)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig(output_image)
plt.close()
