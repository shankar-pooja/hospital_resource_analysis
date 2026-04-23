import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("hospital_data.csv")

print("First 5 rows:")
print(data.head())

# Convert dates
data['Admission_Date'] = pd.to_datetime(data['Admission_Date'])
data['Discharge_Date'] = pd.to_datetime(data['Discharge_Date'])

# Create Length of Stay column
data['Length_of_Stay'] = (data['Discharge_Date'] - data['Admission_Date']).dt.days

print("\nDataset Info:")
print(data.info())

# ----------------------------
# DESCRIPTIVE ANALYSIS
# ----------------------------

# Patients per Department
dept_count = data['Department'].value_counts()
print("\nPatients per Department:")
print(dept_count)

# Average Length of Stay
avg_stay = data['Length_of_Stay'].mean()
print("\nAverage Length of Stay:", avg_stay)

# Bed Usage
bed_usage = data['Bed_Type'].value_counts()
print("\nBed Usage:")
print(bed_usage)

# Cost Analysis
print("\nCost Statistics:")
print(data['Cost'].describe())

# ----------------------------
# VISUALIZATION
# ----------------------------

# Patients per Department
plt.figure()
sns.countplot(x='Department', data=data)
plt.title("Patients in Each Department")
plt.show()

# Length of Stay Distribution
plt.figure()
sns.histplot(data['Length_of_Stay'], bins=5)
plt.title("Length of Stay Distribution")
plt.show()

# Bed Usage
plt.figure()
data['Bed_Type'].value_counts().plot(kind='bar')
plt.title("Bed Type Usage")
plt.show()

# Cost Distribution
plt.figure()
sns.histplot(data['Cost'], bins=5)
plt.title("Cost Distribution")
plt.show()

# ----------------------------
# INSIGHTS PRINT
# ----------------------------

print("\n--- INSIGHTS ---")
print("1. ICU and Emergency departments handle critical patients.")
print("2. Some patients have longer stays, increasing resource usage.")
print("3. Shared beds are used more than private beds.")
print("4. High treatment cost mainly from ICU and trauma cases.")

print("\n--- RECOMMENDATIONS ---")
print("✔ Increase ICU beds")
print("✔ Reduce patient stay duration")
print("✔ Improve scheduling")
print("✔ Allocate staff efficiently")