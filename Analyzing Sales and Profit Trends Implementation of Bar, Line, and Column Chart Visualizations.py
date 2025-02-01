#Analyzing Sales and Profit Trends: Implementation of Bar, Line, and Column Chart Visualizations


#Quantity Sold by Dealer ID 
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = '8cfbf102-4988-496a-ba7c-862497ef3ba0_CarSalesByModelStart.xlsx'

# Read the relevant sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=1)

# Rename columns appropriately
df.columns = ['Dealer ID', 'Sum of Quantity Sold']

# Filter out the 'Grand Total' row
df = df[df['Dealer ID'] != 'Grand Total']

# Convert 'Dealer ID' to numeric, in case it's not
df['Dealer ID'] = pd.to_numeric(df['Dealer ID'], errors='coerce')

# Sort the DataFrame by 'Dealer ID'
df.sort_values('Dealer ID', inplace=True)

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['Dealer ID'].astype(str), df['Sum of Quantity Sold'], color='skyblue')

# Add titles and labels
plt.title('Quantity Sold by Dealer ID', fontsize=16)
plt.xlabel('Dealer ID', fontsize=14)
plt.ylabel('Sum of Quantity Sold', fontsize=14)

# Add value labels on top of bars
for index, value in enumerate(df['Sum of Quantity Sold']):
    plt.text(index, value + 50, str(value), ha='center', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()



#Profit by Date and Model 
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file and read the relevant sheet into a DataFrame
file_path = 'ea0990dd-f486-4902-a834-ca8e04607a7d_CarSalesByModelStart.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet2', skiprows=1)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Drop the 'Grand Total' column for plotting purposes
df.drop(columns=['Grand Total'], inplace=True)

# Plotting
plt.figure(figsize=(14, 7))

for column in df.columns:
    plt.plot(df.index, df[column], label=column, marker='o')

# Add titles and labels
plt.title('Profit by Date and Model', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.legend(title='Car Models')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()



#Profit by Year and Dealer ID
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path = '19cb5ced-f68d-4670-a112-b9293fb46ea1_CarSalesByModelStart.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet3')

# Prepare the data
# Filter out total rows and keep only necessary columns
df = df.dropna(subset=['Unnamed: 1'])
df.columns = ['Year', 'Dealer ID', 'Sum of Profit']
df = df[df['Dealer ID'] != 'Grand Total']

# Convert 'Sum of Profit' to numeric, removing commas if any
df['Sum of Profit'] = df['Sum of Profit'].replace('[\$,]', '', regex=True).astype(float)

# Separate data by year
profits_2018 = df[df['Year'] == 2018]
profits_2019 = df[df['Year'] == 2019]

# Set up the plot
dealer_ids = profits_2018['Dealer ID']
x = np.arange(len(dealer_ids))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(14, 7))

# Plotting columns
rects1 = ax.bar(x - width/2, profits_2018['Sum of Profit'], width, label='2018', color='red')
rects2 = ax.bar(x + width/2, profits_2019['Sum of Profit'], width, label='2019', color='darkred')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Dealer ID')
ax.set_ylabel('Sum of Profit')
ax.set_title('Profit by Year and Dealer ID')
ax.set_xticks(x)
ax.set_xticklabels(dealer_ids)
ax.legend()

# Attach a text label above each bar in rects1 and rects2
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()



#Profit by Hudson Models and Dealer ID  
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'CarSalesByModelStart.xlsx'
sheet_name = 'Sheet4'  # Assuming the relevant data is in Sheet4 based on provided content

# Read the specific sheet into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=1)

# Filter out rows where the Model is 'Hudson'
hudson_df = df[df['Model'] == 'Hudson']

# Extracting necessary columns for the plot
dealer_ids = hudson_df['Dealer ID'].values
profits = hudson_df['Sum of Profit'].values

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(dealer_ids, profits, marker='o', linestyle='-', color='b')

# Adding title and labels
plt.title('Profit of Hudson Models by Dealer ID', fontsize=16)
plt.xlabel('Dealer ID', fontsize=12)
plt.ylabel('Sum of Profit', fontsize=12)

# Display grid for better readability
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()