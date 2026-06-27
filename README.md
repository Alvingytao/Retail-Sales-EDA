# Exploratory Data Analysis on Retail Store Sales Dataset

## 🛒 Project Overview

This project focuses on cleaning and analyzing a Retail Store Sales Dataset to uncover meaningful business insights that can support data-driven decision-making. The dataset contains transaction records including product categories, quantities purchased, prices, payment methods, purchase channels and transaction dates.

The analysis provides insights into sales trends, category performance, revenue growth, payment preferences, purchase channels and overall sales contribution by product category.

## 📝 Problem Statement

Retail businesses generate large volumes of transaction data that can be leveraged to improve business performance. The objective of this project is to:

* Clean and prepare the dataset for analysis.
* Analyze overall sales trends and revenue growth.
* Evaluate the performance of different product categories.
* Examine customer payment methods and purchase channels.
* Identify key business insights that can support decision-making.

## 📂 Dataset

**Source:** Retail Store Sales Dataset

The dataset contains transaction-level information including product categories, item identifiers, quantities sold, unit prices, total spending, payment methods, purchase channels and transaction dates.

## ⚙️ Tools and Technologies

**Programming Language:** Python

**Libraries Used:**

* pandas
* NumPy
* Matplotlib

## 🔍 Key Steps

### Data Loading and Understanding

* Imported the dataset using pandas.
* Explored the dataset using `.info()`, `.describe()` and other inspection methods.
* Identified duplicate records and missing values.

### Data Cleaning

* Removed duplicate records.
* Handled missing values using mathematical relationships between Quantity, Price Per Unit and Total Spent.
* Imputed missing Price Per Unit values using the average price within each Category and Item combination.
* Removed records with irrecoverable missing values.
* Converted transaction dates into a standard datetime format.

### Exploratory Data Analysis (EDA)

* Analyzed yearly sales trends.
* Examined monthly sales trends across different years.
* Calculated yearly revenue contribution.
* Measured overall revenue growth.
* Evaluated category-wise revenue performance.
* Analyzed category growth over time.
* Examined payment method usage.
* Compared in-store and online transactions.
* Calculated average transaction value.
* Determined revenue contribution by product category.

### Data Visualization

* Line Charts: Yearly sales trends and monthly sales trends.
* Horizontal Bar Charts: Revenue by category and category growth.
* Pie Chart: Revenue contribution by category.

## 📈 Visualizations

### Figure 1: Total Sales by Year

![Figure 1](figures/figure_1.png)

### Figure 2: Monthly Sales Trend by Year

![Figure 2](figures/figure_2.png)

### Figure 3: Revenue by Category

![Figure 3](figures/figure_3.png)

### Figure 4: Category Growth (%)

![Figure 4](figures/figure_4.png)

### Figure 5: Revenue Contribution by Category

![Figure 5](figures/figure_5.png)

### Insights and Findings

* Identified the highest and lowest revenue-generating product categories.
* Measured overall business growth across the available years.
* Evaluated the contribution of each category to total revenue.
* Analyzed customer payment preferences.
* Compared purchase channels (In-store vs Online).
* Calculated the average transaction value.

## 📊 Key Insights

* The highest-performing product category was identified.
* Category growth trends were analyzed across complete years.
* Customer payment methods and purchase channels showed relatively balanced distributions.
* Revenue contribution by each product category was determined.
* Monthly and yearly sales trends were analyzed to understand business performance over time.

## 📈 Results

This project demonstrates an end-to-end data analytics workflow including data cleaning, exploratory data analysis and data visualization. The insights generated can help retail businesses understand sales performance, identify high-performing product categories, monitor revenue growth and support data-driven business decisions.
