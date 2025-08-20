# Email: 23f1002802@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Sample employee dataset (sample of 5 rows for example)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,Europe,82.35,14,4.8
EMP002,R&D,Africa,77.59,6,4.9
EMP003,Sales,North America,64.31,8,3.9
EMP004,Sales,North America,92.11,6,4.1
EMP005,Finance,Europe,89.71,11,4.7
"""

# Load data into DataFrame using StringIO
from io import StringIO
df = pd.read_csv(StringIO(data))

# Calculate frequency count for "Finance" department
finance_count = (df['department'] == 'Finance').sum()
print(f"Frequency count for Finance department: {finance_count}")

# Plot department distribution histogram
plt.figure(figsize=(8, 5))
df['department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Department Distribution')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()

# Save interactive visualization as HTML
html_str = mpld3.fig_to_html(plt.gcf())
with open('department_distribution.html', 'w') as f:
    f.write(html_str)

print("Histogram saved as department_distribution.html")
