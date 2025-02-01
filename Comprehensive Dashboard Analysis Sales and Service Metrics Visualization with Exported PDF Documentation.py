import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the Excel file
file_path = 'AU_Sales_By_Model.xlsx'
df = pd.read_excel(file_path)

# Data Processing
total_profit = df['Profit'].sum()
total_quantity_sold = df['Quantity Sold'].sum()
average_quantity_sold = df['Quantity Sold'].mean()

# Group by model to get quantity sold per model
quantity_by_model = df.groupby('Model')['Quantity Sold'].sum().reset_index()

# Create Dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Total Profit", "Total Quantity Sold", 
                    "Quantity Sold by Model", "Average Quantity Sold"),
    specs=[[{"type": "domain"}, {"type": "domain"}],
           [{"type": "xy"}, {"type": "indicator"}]]
)

# Total Profit
fig.add_trace(go.Indicator(
    mode="number",
    value=total_profit,
    title={"text": "Total Profit"},
), row=1, col=1)

# Total Quantity Sold
fig.add_trace(go.Indicator(
    mode="number",
    value=total_quantity_sold,
    title={"text": "Total Quantity Sold"},
), row=1, col=2)

# Quantity Sold by Model (Bar Chart)
fig.add_trace(go.Bar(
    x=quantity_by_model['Model'],
    y=quantity_by_model['Quantity Sold'],
    name='Quantity Sold',
    marker_color='blue'
), row=2, col=1)

# Average Quantity Sold
fig.add_trace(go.Indicator(
    mode="number",
    value=average_quantity_sold,
    title={"text": "Average Quantity Sold"},
), row=2, col=2)

# Update layout for better appearance
fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Sales Dashboard",
    template="plotly_white"
)

# Show the dashboard
fig.show()



import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = '698f6e03-826c-4e85-b548-3ebfbbd4a073_AU_Sales_By_Model.xlsx'
df = pd.read_excel(file_path)

# Group by Dealer ID and sum the profits
profit_by_dealer = df.groupby('Dealer ID')['Profit'].sum().reset_index()

# Sort the DataFrame by Profit in ascending order
profit_by_dealer_sorted = profit_by_dealer.sort_values(by='Profit', ascending=True)

# Plotting
plt.figure(figsize=(12, 8))
plt.barh(profit_by_dealer_sorted['Dealer ID'], profit_by_dealer_sorted['Profit'], color='skyblue')
plt.xlabel('Total Profit')
plt.ylabel('Dealer ID')
plt.title('Total Profit by Dealer ID (Ascending Order)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()



import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'AU_Sales_By_Model.xlsx'
data = pd.read_excel(file_path)

# Recall data
recall_data = {
    'Model': ['Beaufort', 'Salish', 'Labrador', 'Champlain', 'Hudson'],
    'Recalls': [5, 3, 7, 2, 6]
}
recall_df = pd.DataFrame(recall_data)
fig1 = px.bar(recall_df, x='Model', y='Recalls', title='Number of Recalls per Model')
fig1.show()

# Sentiment data
sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [150, 100, 50]
}
sentiment_df = pd.DataFrame(sentiment_data)
fig2 = px.treemap(sentiment_df, path=['Sentiment'], values='Count', title='Customer Sentiment Comparison')
fig2.show()

# Monthly Sales vs Profit
data['Date'] = pd.to_datetime(data['Date'])
monthly_sales = data.groupby(data['Date'].dt.to_period('M')).agg({'Quantity Sold': 'sum', 'Profit': 'sum'}).reset_index()
monthly_sales['Date'] = monthly_sales['Date'].dt.to_timestamp()
fig3 = px.bar(monthly_sales, x='Date', y='Quantity Sold', title='Quantity of Cars Sold per Month')
fig3.add_scatter(x=monthly_sales['Date'], y=monthly_sales['Profit'], mode='lines', name='Profit', yaxis='y2')
fig3.update_layout(yaxis2=dict(overlaying='y', side='right'))
fig3.show()

# Recall by System Heatmap
recall_system_data = {
    'Model': ['Beaufort', 'Beaufort', 'Salish', 'Salish', 'Labrador', 'Labrador'],
    'System': ['Brakes', 'Engine', 'Brakes', 'Transmission', 'Engine', 'Transmission'],
    'Recalls': [3, 2, 1, 2, 4, 3]
}
recall_system_df = pd.DataFrame(recall_system_data)
fig4 = px.density_heatmap(recall_system_df, x='Model', y='System', z='Recalls', nbinsx=5, nbinsy=5, title='Number of Recalls per Model by Affected System')
fig4.show()
