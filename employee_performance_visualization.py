import matplotlib.pyplot as plt
import mpld3

# ... your data loading code ...

fig, ax = plt.subplots(figsize=(8, 5))
df['department'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Department Distribution')
ax.set_xlabel('Department')
ax.set_ylabel('Number of Employees')

# Add your email visibly on the plot
plt.figtext(0.99, 0.01, "Data Scientist: 23f1002802@ds.study.iitm.ac.in", 
            horizontalalignment='right', fontsize=8, alpha=0.7)

plt.tight_layout()

html_str = mpld3.fig_to_html(fig)
with open('department_distribution.html', 'w') as f:
    f.write(html_str)
