import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create figures directory if it doesn't exist
os.makedirs('reports/figures', exist_ok=True)

# Set style for visualizations
sns.set_theme()

# Read the data
df = pd.read_csv('data/raw/car_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 1. Sales Distribution by Engine Type
plt.figure(figsize=(10, 6))
df['Engine_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Engine Types')
plt.axis('equal')
plt.savefig('reports/figures/engine_type_distribution.png')
plt.close()

# 2. Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Price', bins=20)
plt.title('Distribution of Vehicle Prices')
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.savefig('reports/figures/price_distribution.png')
plt.close()

# 3. Sales by Location
plt.figure(figsize=(12, 6))
df['Location'].value_counts().plot(kind='bar')
plt.title('Sales by Location')
plt.xlabel('Location')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/sales_by_location.png')
plt.close()

# 4. Price vs Mileage Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Mileage', y='Price', hue='Engine_Type')
plt.title('Price vs Mileage by Engine Type')
plt.xlabel('Mileage')
plt.ylabel('Price ($)')
plt.tight_layout()
plt.savefig('reports/figures/price_vs_mileage.png')
plt.close()

# 5. Average Price by Make
plt.figure(figsize=(12, 6))
df.groupby('Make')['Price'].mean().sort_values(ascending=False).plot(kind='bar')
plt.title('Average Price by Make')
plt.xlabel('Make')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/avg_price_by_make.png')
plt.close()

# 6. Sales Type Distribution
plt.figure(figsize=(8, 6))
df['Sales_Type'].value_counts().plot(kind='bar')
plt.title('Distribution of Sales Types')
plt.xlabel('Sales Type')
plt.ylabel('Number of Sales')
plt.tight_layout()
plt.savefig('reports/figures/sales_type_distribution.png')
plt.close()

# 7. Registration Status Distribution
plt.figure(figsize=(8, 6))
df['Registration_Status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Registration Status')
plt.axis('equal')
plt.savefig('reports/figures/registration_status_distribution.png')
plt.close()

# 8. Correlation Matrix
plt.figure(figsize=(8, 6))
correlation = df[['Price', 'Mileage', 'Year']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('reports/figures/correlation_matrix.png')
plt.close()

print("All visualizations have been generated in the reports/figures directory.") 