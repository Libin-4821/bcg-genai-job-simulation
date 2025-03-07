#Importing necessary libraries
import pandas as pd
import plotly.express as px

#Loading the dataset
data = pd.read_csv('chatbot/finData.csv') #Check with the file path and change according to the OS

#Sorting data based on Company and year
sorted_data = data.sort_values(by=['Company','Year'])

#Adding new features

#Revenue Growth
sorted_data['Revenue Growth (%)'] = sorted_data.groupby('Company')['Total Revenue'].pct_change() * 100

#Net Income Growth
sorted_data['Net Income Growth (%)'] = sorted_data.groupby('Company')['Net Income'].pct_change() * 100

sorted_data.fillna(0, inplace=True) #filling NaN values

#Net Profit Margin
sorted_data['Net Profit Margin (%)'] = sorted_data['Net Income'] / sorted_data['Total Revenue'] * 100

#Return on Assets
sorted_data['Return On Assets (%)'] = sorted_data['Net Income'] / sorted_data['Total Assets'] * 100

#Asset Turnover Ratio
sorted_data['Asset Turnover Ratio (%)'] = sorted_data['Total Revenue'] / sorted_data['Total Assets'] * 100

#Shareholder Equity
sorted_data['Shareholders\' Equity'] = sorted_data['Total Assets'] - sorted_data['Total Liabilities'] 

#Debt to Equity Ratio
sorted_data['Debt to Equity Ratio (%)'] = sorted_data['Total Liabilities'] / sorted_data['Shareholders\' Equity'] * 100

#Debt to Asset Ratio
sorted_data['Debt to Asset Ratio (%)'] = sorted_data['Total Liabilities'] / sorted_data['Total Assets'] * 100

#Creating Visualizations

#Bar chart - Total Revenue
fig = px.histogram(sorted_data, x="Company", y="Total Revenue",
             color='Year', barmode='group')
fig.show()

#Bar chart - Net Income
fig = px.histogram(sorted_data, x="Company", y="Net Income",
             color='Year', barmode='group')
fig.show()

#Line chart - Debt to Equity Ratio
fig = px.line(sorted_data, x="Year", y="Debt to Equity Ratio (%)",
             color='Company')
fig.update_xaxes(tickvals=sorted_data["Year"])
fig.show()

#Line chart - Debt to Asset Ratio
fig = px.line(sorted_data, x="Year", y="Debt to Asset Ratio (%)",
             color='Company')
fig.update_xaxes(tickvals=sorted_data["Year"])
fig.show()

#Bar chart - Asset Turnover Ratio
fig = px.histogram(sorted_data, x="Company", y="Asset Turnover Ratio (%)",
             color='Year', barmode='group')
fig.show()

#Bar chart - Revenue Growth
fig = px.histogram(sorted_data,x="Year",y="Revenue Growth (%)",color="Company",barmode="group")
fig.show()

#Bar chart - Net Income Growth
fig = px.histogram(sorted_data,x="Year",y="Net Income Growth (%)",color="Company",barmode="group")
fig.show()


