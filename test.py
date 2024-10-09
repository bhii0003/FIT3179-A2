import pandas as pd

# Load your CSV file into a pandas DataFrame
file_path = 'world_data_with_percentage_change.csv'
df = pd.read_csv(file_path)

# Columns to keep: 'entity', 'world', and pollutant percentage columns
columns_to_keep = ['Entity', 'Year', 'Carbon monoxide (CO) emissions (%)', 'Nitrogen oxide (NOx) (%)', 'Sulphur dioxide (SO₂) emissions (%)', 'Non-methane volatile organic compounds (NMVOC) emissions (%)', 'Organic carbon (OC) emissions (%)', 'Black carbon (BC) emissions (%)', 'Ammonia (NH₃) emissions (%)']

# Filter the DataFrame to keep only the relevant columns
df_filtered = df[columns_to_keep]

# Rename pollutant columns by removing 'emissions' and '%' symbol
df_filtered.columns = ['Country', 'Year', 'Carbon monoxide (CO)', 'Nitrogen oxide (NOx)', 'Sulphur dioxide (SO₂)', 'Non-methane volatile organic compounds (NMVOC)', 'Organic carbon (OC)', 'Black carbon (BC)','Ammonia (NH₃)']

# Save the updated DataFrame to a new CSV file
output_file = 'pollutants_percentage.csv'
df_filtered.to_csv(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")
