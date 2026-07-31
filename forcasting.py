import pandas as pd
import numpy as np
from scipy.stats import norm, poisson
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Dataset.csv')


store_id = 'S001'
product_id = 'P0001'

product_data = df[(df['Store ID'] == store_id) & (df['Product ID'] == product_id)]

if product_data.empty:
    print(f"Store {store_id} এবং Product {product_id} এর ডেটা পাওয়া যায়নি, প্রথম ৩৬৫ দিনের ডেটা ব্যবহার করা হচ্ছে।")
    product_data = df.head(365)


daily_demand = product_data['Units Sold']
mu = daily_demand.mean()          
sigma = daily_demand.std()        

print(f"--- Product Analysis for Store: {store_id}, Product: {product_id} ---")
print(f"Average Daily Demand (μ): {mu:.2f}")
print(f"Demand Standard Deviation (σ): {sigma:.2f}\n")


lead_time = 5            
service_level = 0.95     

z_score = norm.ppf(service_level)
safety_stock = z_score * (sigma * np.sqrt(lead_time))
safety_stock = int(np.ceil(safety_stock))

rop = (mu * lead_time) + safety_stock
rop = int(np.ceil(rop))

print(f"Calculated Parameters:")
print(f"-> Z-Score (for {service_level*100}% service level): {z_score:.2f}")
print(f"-> Recommended Safety Stock: {safety_stock} units")
print(f"-> Recommended Reorder Point (ROP): {rop} units\n")

expected_lead_demand = mu * lead_time
poisson_prob = 1 - poisson.cdf(rop, expected_lead_demand)
print(f"Poisson Distribution Stockout Risk during Lead Time: {poisson_prob:.6f}")

plt.figure(figsize=(10, 5))
sns.histplot(daily_demand, kde=True, color='skyblue', stat='density', bins=30, label='Actual Demand Distribution')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'r-', linewidth=2, label='Normal Distribution Fit')

plt.axvline(mu, color='green', linestyle='--', label=f'Mean Demand ({mu:.1f})')
plt.axvline(rop / lead_time, color='purple', linestyle='--', label=f'Avg Daily ROP Level')

plt.title(f'Demand Distribution & Inventory Thresholds for {product_id}')
plt.xlabel('Units Sold / Daily Demand')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()