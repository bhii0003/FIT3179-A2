import pandas as pd

# Load the CSV file
file_path = 'change-air-pollutant-emissions.csv'  # Update with the correct path if needed
df = pd.read_csv(file_path)

# Filter the data to include only rows for the World and years between 1970 and 2022
filtered_df = df[(df['Entity'] == 'World') & (df['Year'] >= 1970) & (df['Year'] <= 2022)]

# Save the filtered data to a new CSV file
filtered_df.to_csv('filtered_world_data_1970_2022.csv', index=False)

print("Data extraction completed and saved to 'filtered_world_data_1970_2022.csv'.")
