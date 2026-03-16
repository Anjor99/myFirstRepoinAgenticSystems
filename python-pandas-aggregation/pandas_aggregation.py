import pandas as pd
import numpy as np

# ------------------------------------
# 1. Create Sample Dataset
# ------------------------------------
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

# ------------------------------------
# 2. Detect Missing Values
# ------------------------------------
print("Missing Values in Each Column:")
print(df.isnull().sum())
print()

# ------------------------------------
# 3. Fill Missing Salary with Mean
# ------------------------------------
salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

print("Dataset After Filling Missing Salary:")
print(df)
print()

# ------------------------------------
# 4. Drop Temporary_Notes Column
# ------------------------------------
df_clean = df.drop(columns=["Temporary_Notes"])

print("Dataset After Dropping Temporary_Notes:")
print(df_clean)
print()

# ------------------------------------
# 5. Rename Salary Column
# ------------------------------------
df_clean = df_clean.rename(columns={"Salary": "Annual_Salary"})

print("Dataset After Renaming Column:")
print(df_clean)
print()

# ------------------------------------
# 6. Group by Department
# ------------------------------------
summary = df_clean.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("Department Summary Table:")
print(summary)