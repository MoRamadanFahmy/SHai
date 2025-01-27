
import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('/content/Salaries.csv', error_bad_lines=False)
df.head()

df.columns

#basic Data Exploration

#number of rows and columns

num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

print("---------------------------------------")

# Display data types of each column
data_types = df.dtypes
print("\nData types of each column:")
print(data_types)
print("---------------------------------------")

# Check for missing values in each column

missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

#Descriptive Statistics

mean_salary = df['TotalPay'].mean()
median_salary = df['TotalPay'].median()
mode_salary = df['TotalPay'].mode()[0]  # Mode can be a Series, take the first value
min_salary = df['TotalPay'].min()
max_salary = df['TotalPay'].max()
salary_range = max_salary - min_salary
std_dev_salary = df['TotalPay'].std()


print(f"Mean Salary: {mean_salary:.2f}")
print(f"Median Salary: {median_salary:.2f}")
print(f"Mode Salary: {mode_salary:.2f}")
print(f"Minimum Salary: {min_salary:.2f}")
print(f"Maximum Salary: {max_salary:.2f}")
print(f"Salary Range: {salary_range:.2f}")
print(f"Standard Deviation of Salary: {std_dev_salary:.2f}")

#handling missing values
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)
#as the number of missing values is not low we cant just delete the rows n columns so we will just fill it with the mean

# Impute missing values with the mean
df['BasePay'].fillna(df['BasePay'].mean(), inplace=True)
df['TotalPay'].fillna(df['TotalPay'].mean(), inplace=True)


#i droped notes & status column as most of them were missing values
df['Agency'].fillna(value=0, inplace=True)
df['Benefits'].fillna(value=0, inplace=True)
df['TotalPayBenefits'].fillna(value=0, inplace=True)
df['OvertimePay'].fillna(value=0, inplace=True)
df['Year'].fillna(value=2011, inplace=True)
df['OtherPay'].fillna(value=0, inplace=True)

#Basic Data Visualization
import matplotlib.pyplot as plt

# Visualization of Salary Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df['TotalPay'], bins=20, color='blue', alpha=0.7)
plt.title('Salary Distribution')
plt.xlabel('TotalPay')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

grouped_data = df.groupby('OtherPay')['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max'])

# Display the grouped summary statistics
print(grouped_data)


plt.figure(figsize=(10, 6))
plt.bar(grouped_data.index, grouped_data['mean'], color='skyblue')
plt.title('Average Salary Across Different Departments')
plt.xlabel('OtherPay')
plt.ylabel('TotalPay')
plt.show()

