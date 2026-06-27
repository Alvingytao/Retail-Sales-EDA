import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Loading the dataset
df = pd.read_csv(r"C:\Users\PC\Downloads\retail_store.csv", encoding="latin1")

#INSPECTING THE DATA
#print(df.info())
#print(df.describe())

#REMOVING DUPLICATES
df = df.drop_duplicates()

#DEALING WITH MISSING VALUES
#print(df.isna().sum())

#total_spent = quantity * price_per_unit
#quantity = total_spent / price_per_unit
#price_per_unit = total_spent /quantity

#Populating the data
mask = (
    df['Quantity'].notna()
    & df['Total Spent'].isna()
    & df['Price Per Unit'].notna()
)
#print(mask.sum())

#Populating Price per unit 
mask = (df['Price Per Unit'].isna()
        &df['Quantity'].notna()
        &df['Total Spent'].notna())

df.loc[mask,'Price Per Unit']= (df.loc[mask,'Total Spent']/df.loc[mask,'Quantity'])

#Dropping multiple column missing values
df = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent'],how='all')
df = df.dropna(subset=['Quantity', 'Total Spent'],how='all')

#Populating price per unit using item id
x = df.groupby(['Category','Item'])['Price Per Unit'].describe()

means = df.groupby(['Category','Item'])['Price Per Unit'].transform('mean')
df['Price Per Unit'] = df['Price Per Unit'].fillna(means)

#Dealing with mixed date time
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df = df.sort_values('Transaction Date')
#print(df['Transaction Date'].head(40))

#EDA
#Trends
yearly_spent = df.groupby(df['Transaction Date'].dt.year)['Total Spent'].sum()
#print(Overall_Trend)

Total_spent = yearly_spent.sum()
percent_yearly_contribution = yearly_spent/Total_spent * 100
projected_2025 = 25548*12*4/3
#408768.0

#Growth
Sales_growth = 524881.0-510329.5
Overall_growth_pct = Sales_growth/510329.5 *100
#2.852

Yearly_categories_sum = df.groupby(['Category',df['Transaction Date'].dt.year])['Total Spent'].sum()
Total_category_sum = Yearly_categories_sum.sum()
df_complete = df[df['Transaction Date'].dt.year != 2025]

pivot = df_complete.pivot_table(
    values='Total Spent',
    index='Category',
    columns=df_complete['Transaction Date'].dt.year,
    aggfunc='sum')

Category_growth = ((pivot.iloc[:, -1] - pivot.iloc[:, 0]) / pivot.iloc[:, 0]) * 100
#hghest = bvg 16.75,comp and electric accesories 16.090
#lowest = butchers -16.79

#Perfomance of each product category
total_category_sum = df.groupby(['Category'])['Total Spent'].sum()
pct_category_share = total_category_sum/Total_spent * 100

monthly_sales = (df.groupby(df['Transaction Date'].dt.to_period('M'))['Total Spent'].sum())

#print(Total_category_sum)
max_category_overall = total_category_sum.idxmax()
#Butchers 208118.0
min_category_overall = total_category_sum.min()
#Milk products 180112.0

location = df['Location'].value_counts()
#instore largely similar to online purchases w online  being slightly more
payment = df['Payment Method'].value_counts()
#same w cash being used slighly more

avg_transaction_value= df['Total Spent'].mean()
sales_by_pay = df.groupby(['Payment Method'])['Total Spent'].mean()
#around 130 w highest being cash by 2$ and avg spend being 129
quant_sold = df.groupby(['Category'])['Quantity'].sum()
min_quant = quant_sold.idxmax()
#Ptisserie,max=funiture
#print(min_quant)

#Bitrate analysis
#print(pd.crosstab(df['Category'], df['Location']))
#print(pd.crosstab(df['Category'], df['Payment Method']))
#print(pd.crosstab(df['Location'], df['Payment Method']))



#VISUALIZATION
#Total sales by year
yearly_val = yearly_spent.values
years = yearly_spent.index.astype(str)
plt.plot(years,yearly_val)
plt.grid('True')
plt.title("Total Sales by Year")
plt.xlabel("Years")
plt.ylabel("Sales")

#total sales by month acrossthe years
monthly_trend = df.pivot_table(
    values='Total Spent',
    index=df['Transaction Date'].dt.month,
    columns=df['Transaction Date'].dt.year,
    aggfunc='sum')
plt.figure(figsize=(10,5))
for year in monthly_trend.columns:
    plt.plot(monthly_trend.index, monthly_trend[year], marker='o', label=year)
plt.xticks(range(1,13),['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend by Year")
plt.legend()
plt.grid(True)

#Revenue by Category
plt.figure(figsize=(8,5))
plt.barh(total_category_sum.index, total_category_sum.values)
plt.title("Revenue by Category")
plt.xlabel("Total Revenue")
plt.ylabel("Category")

#plt.show()
growth = Category_growth.sort_values()
plt.figure(figsize=(8,5))
plt.barh(growth.index, growth.values)
plt.title("Category Growth (%)")
plt.xlabel("Growth (%)")
plt.ylabel("Category")

#Sales contribution by category
category_percent = (total_category_sum / total_category_sum.sum()) * 100
plt.figure(figsize=(6,6))
plt.pie(
    category_percent.values,
    labels=category_percent.index,
    autopct='%1.1f%%',
    startangle=90)

plt.title("Revenue Contribution by Category")
plt.show()


df.to_csv(r"C:\Users\PC\Downloads\retail_store.csv", index = False)