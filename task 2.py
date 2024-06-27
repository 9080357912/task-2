1)

import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Get some basic information
print(df.head())
print(df.shape)

# Select specific columns and filter rows
selected_df = df[["column_A", "column_B"]][df["column_C"] > 10]

# Add a new column and modify another
selected_df["column_D"] = selected_df["column_A"] + selected_df["column_B"]
selected_df["column_B"] = selected_df["column_B"].astype(str)

# Save the modified data
selected_df.to_csv("processed_data.csv", index=False)

2)
import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values in "column_A"
df = df.dropna(subset=["column_A"])

# Fill missing values in "column_B" with the mean
df["column_B"] = df["column_B"].fillna(df["column_B"].mean())

# Remove duplicate rows
df = df.drop_duplicates()


3)


# Filter rows where Age > 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)
# Sort by Salary in descending order
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted DataFrame (by Salary, descending):")
print(sorted_df)
# Group by Department and calculate the average Salary
grouped_df = df.groupby('Department')['Salary'].mean().reset_index()
print("\nGrouped DataFrame (average Salary by Department):")
print(grouped_df)


