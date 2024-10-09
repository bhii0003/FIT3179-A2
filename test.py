# Let's load the uploaded CSV file and inspect its structure to confirm the data and prepare the code to calculate the percentage change and create a Vega-Lite compatible JSON for the graph.

import pandas as pd

# Load the filtered world data CSV file
file_path = 'filtered_world_data_1970_2022.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
data.head()

# Calculate the percentage change relative to the year 1970 for each pollutant.
# We'll select the 1970 row as the baseline and calculate the change for subsequent years.

baseline = data[data['Year'] == 1970].iloc[0]  # Baseline values for the year 1970

# List of columns with emissions data
pollutants = [
    'Carbon monoxide (CO) emissions',
    'Nitrogen oxide (NOx)',
    'Sulphur dioxide (SO₂) emissions',
    'Non-methane volatile organic compounds (NMVOC) emissions',
    'Organic carbon (OC) emissions',
    'Black carbon (BC) emissions',
    'Ammonia (NH₃) emissions'
]

# Calculate percentage change for each pollutant
for pollutant in pollutants:
    data[pollutant + ' (%)'] = ((data[pollutant] - baseline[pollutant]) / baseline[pollutant]) * 100

# Save the resulting DataFrame to a new CSV file
output_file = 'world_data_with_percentage_change.csv'
data.to_csv(output_file, index=False)

data.head()  # Display the first few rows to verify the percentage change columns
