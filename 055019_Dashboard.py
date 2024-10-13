# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
data = pd.read_csv("group_project.csv")
data['Total_Value'] = data['Value'] * data['Quantity']
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y', errors='coerce')
data['Year'] = data['Date'].dt.year

# Sample data for performance
sample_data = data.sample(n=3001, random_state=55004)

# Title and description
st.title("🌍 Global Trade Insights Dashboard")
st.markdown("""
This dashboard provides an interactive analysis of international trade trends from imports and exports.
Explore trade data by year, category, country, and more. Visualizations highlight key insights into the trade distribution.
""")

# Summary Metrics
st.markdown("### Key Metrics")
col1, col2, col3 = st.columns(3)
total_trade_value = sample_data['Total_Value'].sum()
total_quantity = sample_data['Quantity'].sum()
total_transactions = sample_data.shape[0]

col1.metric("Total Trade Value", f"${total_trade_value:,.2f}")
col2.metric("Total Quantity", f"{total_quantity}")
col3.metric("Total Transactions", f"{total_transactions}")

st.markdown("---")

# Visualization 1: Sunburst Chart for Trade Breakdown by Category and Import/Export Type
st.subheader("1. Trade Breakdown by Category and Import/Export Type")
st.markdown("**Interpretation:** This sunburst chart shows the distribution of total trade value across various categories, segmented by import and export. Larger sections indicate higher trade values.")
category_import_export = sample_data.groupby(['Category', 'Import_Export'])['Total_Value'].sum().reset_index()
fig_sunburst = px.sunburst(category_import_export, path=['Category', 'Import_Export'], values='Total_Value',
                           title="Trade Breakdown by Category and Import/Export", color='Total_Value', 
                           color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig_sunburst)

# Visualization 2: Yearly Trade Volume Trend
st.subheader("2. Yearly Trade Volume Trend")
st.markdown("**Interpretation:** The line chart illustrates how the trade volume has changed over the years for both imports and exports. Peaks in the graph indicate periods of increased trade activity.")
yearly_trend = sample_data.groupby(['Year', 'Import_Export'])['Total_Value'].sum().reset_index()
fig_yearly_trend = px.line(yearly_trend, x='Year', y='Total_Value', color='Import_Export', markers=True,
                           title="Yearly Trade Volume Trend", labels={'Total_Value': 'Total Trade Value'},
                           color_discrete_sequence=px.colors.qualitative.Pastel)
fig_yearly_trend.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_yearly_trend)

# Visualization 3: Treemap of Top Countries by Trade Value
st.subheader("3. Top Countries by Trade Value")
st.markdown("**Interpretation:** This treemap highlights the countries with the highest trade value. Each country's box size represents its share of the total trade value.")
top_countries = sample_data.groupby('Country')['Total_Value'].sum().sort_values(ascending=False).head(15).reset_index()
fig_treemap = px.treemap(top_countries, path=['Country'], values='Total_Value',
                         title="Top 15 Countries by Trade Value", color='Total_Value', 
                         color_continuous_scale=px.colors.sequential.Sunset)
st.plotly_chart(fig_treemap)

# Visualization 4: Top 10 Products by Trade Value
st.subheader("4. Top 10 Products by Trade Value")
st.markdown("**Interpretation:** The bar chart shows the top 10 products in terms of trade value. This helps to identify the most economically significant products in the dataset.")
top_products = sample_data.groupby('Product')['Total_Value'].sum().sort_values(ascending=False).head(10).reset_index()
fig_products = px.bar(top_products, x='Product', y='Total_Value', color='Product', 
                      title="Top 10 Products by Trade Value", color_discrete_sequence=px.colors.qualitative.Safe)
fig_products.update_layout(xaxis_title='Product', yaxis_title='Total Trade Value', title_x=0.5)
st.plotly_chart(fig_products)

# Visualization 5: Scatter Plot of Weight vs. Value
st.subheader("5. Weight vs. Value of Trades")
st.markdown("**Interpretation:** This scatter plot shows the relationship between the weight and value of trades across different categories. Larger bubbles represent higher total trade values.")
fig_scatter = px.scatter(sample_data, x='Weight', y='Value', size='Total_Value', color='Category', 
                         title="Scatter Plot of Weight vs Value", labels={'Value': 'Trade Value'},
                         color_discrete_sequence=px.colors.qualitative.Dark2, opacity=0.7)
fig_scatter.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_scatter)

# Visualization 6: Geographic Distribution of Trade Value
st.subheader("6. Geographic Distribution of Trade Value")
st.markdown("**Interpretation:** The choropleth map provides a geographic distribution of trade value by country. Darker shades indicate higher trade values, allowing for easy regional comparison.")
fig_choropleth = px.choropleth(sample_data, locations='Country', locationmode='country names', 
                               color='Total_Value', hover_name='Country', 
                               title="Trade Value by Country", color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig_choropleth)

# Additional Visualization 7: Trade Balance by Country
st.subheader("7. Trade Balance by Country")
st.markdown("**Interpretation:** This bar chart displays the trade balance (exports - imports) for each country, indicating whether they are net exporters or net importers.")
trade_balance = sample_data.groupby(['Country', 'Import_Export'])['Total_Value'].sum().unstack().fillna(0)
trade_balance['Trade_Balance'] = trade_balance['Export'] - trade_balance['Import']
trade_balance = trade_balance.sort_values(by='Trade_Balance', ascending=False).reset_index()
fig_trade_balance = px.bar(trade_balance, x='Country', y='Trade_Balance', title="Trade Balance by Country",
                           color='Trade_Balance', color_continuous_scale='tealrose')
st.plotly_chart(fig_trade_balance)

# Additional Visualization 8: Monthly Trade Value Trend
st.subheader("8. Monthly Trade Value Trend")
st.markdown("**Interpretation:** This line chart shows the monthly trend in trade values for imports and exports, revealing seasonal patterns and monthly fluctuations.")
sample_data['Month'] = sample_data['Date'].dt.strftime('%Y-%m')  # Convert to string format
monthly_trend = sample_data.groupby(['Month', 'Import_Export'])['Total_Value'].sum().reset_index()
fig_monthly_trend = px.line(monthly_trend, x='Month', y='Total_Value', color='Import_Export', markers=True,
                            title="Monthly Trade Value Trend", labels={'Total_Value': 'Total Trade Value'},
                            color_discrete_sequence=px.colors.qualitative.Pastel)
fig_monthly_trend.update_layout(xaxis_title='Month', yaxis_title='Trade Value')
st.plotly_chart(fig_monthly_trend)

# Additional Visualization 9: Trade Value by Category for Top Countries
st.subheader("9. Trade Value by Category for Top Countries")
st.markdown("**Interpretation:** This stacked bar chart visualizes the distribution of trade values across categories for the top 10 countries, highlighting which products are the primary drivers of trade in each country.")
top_countries_list = trade_balance.head(10)['Country'].tolist()
category_top_countries = sample_data[sample_data['Country'].isin(top_countries_list)]
category_trade = category_top_countries.groupby(['Country', 'Category'])['Total_Value'].sum().reset_index()
fig_category_country = px.bar(category_trade, x='Country', y='Total_Value', color='Category', barmode='stack',
                              title="Trade Value by Category for Top Countries")
st.plotly_chart(fig_category_country)

# Download Filtered Data
if st.button("Download Sampled Data"):
    sample_data.to_csv("sampled_trade_data.csv", index=False)
    st.success("Data has been saved as 'sampled_trade_data.csv'")
