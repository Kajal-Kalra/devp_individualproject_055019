# Global Trade Insights Dashboard

## Project Overview
This project provides a comprehensive analysis of international trade data using Python and data visualization libraries such as Pandas, Numpy, Matplotlib, Plotly, and Streamlit. The dashboard allows users to interactively explore trade trends, understand patterns, and gain insights into trade distribution across categories, countries, and years.

## Problem Statement
The primary goal of this project is to understand the drivers of trade flow efficiency through the analysis of various trade components such as supplier behavior, payment terms, and order timing patterns. The study identifies key trends in international trade, uncovers trade flow dynamics, and assesses frequently traded goods. Additionally, it highlights seasonal and regional variations to derive actionable insights for optimizing trade operations.

## Key Features
- **Interactive Dashboard**: Built with Streamlit, the dashboard enables users to explore trade data by filtering through years, categories, and countries. Visualizations include bar charts, line charts, sunburst charts, scatter plots, and more.
- **Trade Analysis**: Provides insights into high-value products, top exporting and importing countries, seasonal trends, and payment term preferences.
- **Statistical Analysis**: Employs statistical tests and summary statistics to explore trade patterns and relationships between variables.
- **Recommendations**: Based on the analysis, the project provides strategic recommendations for optimizing trade flows and identifying market opportunities.

## Dashboard Overview
To run the dashboard, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies by running the following command: `pip install pandas numpy matplotlib seaborn plotly streamlit`
3. Start the Streamlit app by running the following command: `streamlit run 055019_Dashboard_Devp.py`

The dashboard includes the following visualizations:

- **Sunburst Chart**: Visualizes trade breakdown by category and type (import/export).
- **Yearly Trend Line Chart**: Shows how trade volume has changed over the years.
- **Treemap of Countries**: Highlights the top countries by trade value.
- **Bar Chart of Top Products**: Displays the highest value products traded.
- **Scatter Plot**: Plots weight vs. value of trades to explore the relationship between the two.
- **Choropleth Map**: Shows the geographic distribution of trade value by country.
- **Trade Balance Analysis**: Illustrates whether countries are net exporters or importers.

## Analysis Report
In addition to the dashboard, the project includes an in-depth data analysis notebook. The notebook covers:

- **Descriptive Statistics**: Analysis of trade value, quantity, and weight using measures of central tendency, dispersion, and correlation.
- **Yearly & Monthly Trends**: Analysis of seasonal and annual trade patterns.
- **Product & Market Insights**: Identification of top import and export products, key markets, and shipping method preferences.
- **Statistical Testing**: Application of ANOVA, normality tests, and correlation analysis to better understand trade data.
- **Observations and Recommendations**: The notebook concludes with a set of observations, managerial insights, and strategic recommendations based on the analysis.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
