import pandas as pd
import datetime as dt
store=pd.read_excel('samplesuperstore.xlsx')
print(store.info())
print(store.isnull().sum())
#Analysis
#Total Business Analysis
print("Total Sales:",store['Sales'].sum())
print("Total Profit:",store['Profit'].sum())
print("Total Order:",store['Order ID'].nunique())
#Sales by Category
print(store.groupby('Category')['Sales'].sum().sort_values(ascending=False))
#Profit by category
print(store.groupby('Category')['Profit'].sum().sort_values(ascending=False))
#Sales by Region
print(store.groupby('Region')['Sales'].sum().sort_values(ascending=False))
#Monthly Sales Trend
store["Month"]=store["Order Date"].dt.to_period("M")
print(store.groupby("Month")["Sales"].sum())
#TOp 10 Product
print(store.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(11))
#profit Vs Sales
print(store.groupby('Category')[['Sales','Profit']].sum())
print(store.to_excel('Cleaned Store.xlsx'))
