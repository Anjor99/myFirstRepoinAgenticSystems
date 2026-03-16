import pandas as pd

# -----------------------------
# 1. Create a sample dataset
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [95, 92, 78, 88, 84],
    "Passed": [True, True, False, True, False],
    "Category": ["A", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

# -----------------------------
# 2. Select a single column
# -----------------------------
print("Single Column (Name):")
print(df["Name"])
print()

# -----------------------------
# 3. Select multiple columns
# -----------------------------
selected_df = df[["Name", "Score"]]

print("Selected Columns (Name and Score):")
print(selected_df)
print()

# -----------------------------
# 4. Use iloc to retrieve first three rows
# -----------------------------
print("First three rows using iloc:")
print(df.iloc[0:3])
print()

# -----------------------------
# 5. Use loc after setting index
# -----------------------------
df_indexed = df.set_index("Name")

print("Using loc after setting Name as index:")
print(df_indexed.loc["Alice"])
print()

# -----------------------------
# 6. Filter rows where Score > 85
# -----------------------------
high_score = df[df["Score"] > 85]

print("Students with Score > 85:")
print(high_score)
print()

# -----------------------------
# 7. Filter rows where Score > 85 AND Passed is True
# -----------------------------
high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Students with Score > 85 and Passed:")
print(high_passed)
print()

# -----------------------------
# 8. Sort filtered result by Score (descending)
# -----------------------------
sorted_high = high_passed.sort_values(by="Score", ascending=False)

print("Sorted High Performers (Descending Score):")
print(sorted_high)
print()

# -----------------------------
# 9. Chained filtering + sorting
# -----------------------------
print("High-performing students (Score > 85 and Passed):")
result = df[(df["Score"] > 85) & (df["Passed"] == True)] \
            .sort_values(by="Score", ascending=False)[["Name", "Score"]]

print(result)