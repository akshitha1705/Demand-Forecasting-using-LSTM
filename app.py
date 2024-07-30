import streamlit as st
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM

# Custom LSTM class without the 'time_major' argument, if necessary
class CustomLSTM(LSTM):
    def __init__(self, **kwargs):
        kwargs.pop('time_major', None)  # Remove 'time_major' if present
        super().__init__(**kwargs)

# Load the model with custom objects
model = load_model("D:/seasonal_sales_model.h5", custom_objects={"LSTM": CustomLSTM})

# Load the dataset containing predictions
data = pd.read_csv("D:/predicted_sales_2023_monthly (1).csv")

# Combine year and month to create a date column if not already present
data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Set up the title and description
st.markdown("""
    <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">Fashion Product Demand Forecasting</h1>
    </div>
""", unsafe_allow_html=True)

st.write("Select a product to view the predicted sales for 2023.")

# Dropdown menu for selecting the product
product_names = data['product_name'].unique()
selected_product = st.selectbox("Select a product:", product_names)

# Filter the data for the selected product
product_data = data[data['product_name'] == selected_product]

# Display the product's predicted sales
st.write(f"<h2>Predicted Sales Data for {selected_product}</h2>", unsafe_allow_html=True)

# Choose chart type
chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart", "Histogram", "Pie Chart"])

# Custom Colors for Bar Chart
custom_colors = px.colors.qualitative.Plotly

if chart_type == "Line Chart":
    fig = px.line(product_data, x='Date', y='Predicted_sales_count', title=f'Sales Trend for {selected_product}')
elif chart_type == "Bar Chart":
    # Assign colors to bars
    fig = px.bar(product_data, x='Date', y='Predicted_sales_count', title=f'Sales Bar Chart for {selected_product}',
                color='Month',  # Use a column to assign colors
                color_discrete_sequence=custom_colors)
elif chart_type == "Area Chart":
    fig = px.area(product_data, x='Date', y='Predicted_sales_count', title=f'Sales Area Chart for {selected_product}')
elif chart_type == "Histogram":
    fig = px.histogram(product_data, x='Predicted_sales_count', title=f'Sales Histogram for {selected_product}')
elif chart_type == "Pie Chart":
    fig = px.pie(product_data, names='Month', values='Predicted_sales_count', title=f'Sales Distribution by Month for {selected_product}')

fig.update_layout(xaxis_title='Date', yaxis_title='Predicted Sales Count')
st.plotly_chart(fig)

# Display evaluation metrics
mae = 10.5  # Replace with actual calculation
rmse = 15.2  # Replace with actual calculation

st.markdown(f"""
    <div style="background-color: #f9f9f9; padding: 10px; border-radius: 10px; margin-top: 20px;">
        <h3>Evaluation Metrics</h3>
        <p><b>Mean Absolute Error (MAE):</b> {mae}</p>
        <p><b>Root Mean Squared Error (RMSE):</b> {rmse}</p>
    </div>
""", unsafe_allow_html=True)

# Additional custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stSelectbox label {
            color: #333;
            font-weight: bold;
        }
        .stDataFrame, .stChart {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Product Comparison
st.write("Compare sales data for different products.")
compare_products = st.multiselect("Select products to compare:", product_names)

if len(compare_products) > 1:
    compare_data = data[data['product_name'].isin(compare_products)]
    fig_compare = px.line(compare_data, x='Date', y='Predicted_sales_count', color='product_name',
                         title='Sales Comparison of Selected Products')
    fig_compare.update_layout(xaxis_title='Date', yaxis_title='Predicted Sales Count')
    st.plotly_chart(fig_compare)

# Download Data
st.write("Download the displayed data.")
if st.button('Download Data'):
    csv = product_data.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name=f'{selected_product}_predicted_sales.csv')

# Summary Statistics
st.write("Summary Statistics")
summary_stats = product_data.describe().T[['mean', '50%', 'std', 'min', 'max']]
st.dataframe(summary_stats)

# Add Interactive Sliders
st.write("Select a range of months to view data.")
month_range = st.slider("Select Month Range", min_value=1, max_value=12, value=(1, 12))
monthly_data = product_data[product_data['Month'].between(month_range[0], month_range[1])]
fig_monthly = px.line(monthly_data, x='Date', y='Predicted_sales_count', title='Monthly Sales Data')
fig_monthly.update_layout(xaxis_title='Date', yaxis_title='Predicted Sales Count')
st.plotly_chart(fig_monthly)
