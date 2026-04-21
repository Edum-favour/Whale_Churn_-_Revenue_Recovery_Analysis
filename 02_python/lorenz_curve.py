import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('thewhales_data.csv')

plt.style.use('dark_background')

plt.plot(df['customer_percentage_rank'], df['cumulative_revenue_pct'], label='Lorenz Curve')

plt.plot([0,100], [0,100], linestyle='--', label='Perfect Equality')

plt.xlabel('Cumulative % of Customers')
plt.ylabel('Cumulative % of Revenue')
plt.title('Lorenz Curve: Customer Revenue Distribution')

plt.legend()

plt.grid(alpha=0.2)

plt.show()