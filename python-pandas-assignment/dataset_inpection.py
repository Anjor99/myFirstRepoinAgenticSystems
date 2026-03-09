import pandas as pd

print("Loading dataset...\n")

# Load CSV file
df = pd.read_csv("ai_dataset.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())
print()

# Display last 5 rows
print("Last 5 rows:")
print(df.tail())
print()

# Dataset structure information
print("Dataset Info:")
df.info()
print()

# Summary statistics
print("Summary Statistics:")
print(df.describe())
print()

# Select single column
age_column = df["Age"]

print("Single Column Selected (Age):")
print(age_column)
print()

# Select multiple columns
selected_columns = df[["Age", "Score"]]

print("Multiple Columns Selected (Age and Score):")
print(selected_columns)
print()

# Filter rows based on numerical condition
filtered_rows = df[df["Score"] > 80]

print("Filtered Rows (Score > 80):")
print(filtered_rows)
print()