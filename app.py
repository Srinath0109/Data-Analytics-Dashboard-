import streamlit as st
import pandas as pd
import visualizations as vz
from data_loader import load_data

# App Title
st.title("📊 Data Analytics Dashboard")

# Upload dataset
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)

    # Show data summary
    st.subheader("Dataset Preview")
    st.write(data.head())

    # Visualization options
    option = st.selectbox(
        "Choose an Analysis",
        ["Sales Trends", "Category Distribution", "Top Performers"]
    )

    if option == "Sales Trends":
        st.pyplot(vz.plot_sales_trends(data))

    elif option == "Category Distribution":
        st.pyplot(vz.plot_category_distribution(data))

    elif option == "Top Performers":
        st.pyplot(vz.plot_top_performers(data))
