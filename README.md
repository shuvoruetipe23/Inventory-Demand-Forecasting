1. Project Title:
Smart Inventory Optimization & Demand Forecasting Model

2. Short Tagline / One-Liner:
A data-driven inventory management system leveraging statistical distributions (Normal & Poisson) to optimize safety stock, calculate reorder points, and minimize supply chain holding costs.

3. Tech Stack / Tools Used:
Programming Language: Python

Libraries: Pandas, NumPy, SciPy, Matplotlib, Seaborn

Concepts: Demand Forecasting, Normal Distribution, Poisson Distribution, Safety Stock, Reorder Point (ROP), Service Level Optimization.

4. Project Overview (Description):
Traditional inventory management often suffers from stockouts or excessive holding costs due to demand uncertainty. This project develops a robust statistical model using historical retail and supply chain data. By applying Normal and Poisson distributions, the model accurately analyzes demand variability during lead times, determines optimal Safety Stock thresholds, and automates Reorder Point (ROP) calculations to ensure seamless supply chain operations at a 95% service level.

5. Key Features & Implementation:
Demand Distribution Analysis: Analyzed historical sales data (Units Sold) to compute mean daily demand and standard deviations, fitting theoretical distribution curves.

Safety Stock Optimization: Implemented Z-score and lead-time variability formulas to calculate exact buffer stocks preventing unexpected stockouts.

Automated ROP Generation: Built logic to trigger reorders precisely when inventory hits critical thresholds.

Data Visualization: Generated automated distribution and probability plots using Matplotlib and Seaborn to visualize actual sales vs. theoretical demand thresholds.
