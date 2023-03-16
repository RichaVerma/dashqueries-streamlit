
import streamlit as st
import pandas as pd
import numpy as np
import json

st.title('Dashqueries: Analyzing Opportunities by Sales Medium')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/RichaVerma/dashqueries-streamlit/blob/main/data.json')

json_data =  [{"b2b_sales_medium": "Enterprise Sellers", "city": "Bengaluru", "max": 132}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Chennai", "max": 128}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Delhi", "max": 148}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Hyderabad", "max": 116}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Kolkata", "max": 134}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Mumbai", "max": 130}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Pune", "max": 114}, {"b2b_sales_medium": "Marketing", "city": "Bengaluru", "max": 138}, {"b2b_sales_medium": "Marketing", "city": "Chennai", "max": 104}, {"b2b_sales_medium": "Marketing", "city": "Delhi", "max": 137}, {"b2b_sales_medium": "Marketing", "city": "Hyderabad", "max": 121}, {"b2b_sales_medium": "Marketing", "city": "Kolkata", "max": 91}, {"b2b_sales_medium": "Marketing", "city": "Mumbai", "max": 92}, {"b2b_sales_medium": "Marketing", "city": "Pune", "max": 210}, {"b2b_sales_medium": "Online Leads", "city": "Bengaluru", "max": 75}, {"b2b_sales_medium": "Online Leads", "city": "Chennai", "max": 45}, {"b2b_sales_medium": "Online Leads", "city": "Delhi", "max": 91}, {"b2b_sales_medium": "Online Leads", "city": "Hyderabad", "max": 72}, {"b2b_sales_medium": "Online Leads", "city": "Kolkata", "max": 39}, {"b2b_sales_medium": "Online Leads", "city": "Mumbai", "max": 48}, {"b2b_sales_medium": "Online Leads", "city": "Pune", "max": 47}, {"b2b_sales_medium": "Partners", "city": "Bengaluru", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Chennai", "max": 83}, {"b2b_sales_medium": "Partners", "city": "Delhi", "max": 125}, {"b2b_sales_medium": "Partners", "city": "Hyderabad", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Kolkata", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Mumbai", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Pune", "max": 90}, {"b2b_sales_medium": "Tele Sales", "city": "Bengaluru", "max": 85}, {"b2b_sales_medium": "Tele Sales", "city": "Chennai", "max": 40}, {"b2b_sales_medium": "Tele Sales", "city": "Delhi", "max": 91}, {"b2b_sales_medium": "Tele Sales", "city": "Hyderabad", "max": 70}, {"b2b_sales_medium": "Tele Sales", "city": "Kolkata", "max": 73}, {"b2b_sales_medium": "Tele Sales", "city": "Mumbai", "max": 85}, {"b2b_sales_medium": "Tele Sales", "city": "Pune", "max": 77}]
sql = "\n\nSELECT b2b_sales_medium, city, MAX(sales_velocity) \nFROM sales_data \nGROUP BY b2b_sales_medium, city \nORDER BY b2b_sales_medium, city NULLS LAST;"

def load_data():
  return pd.DataFrame([{"b2b_sales_medium": "Enterprise Sellers", "city": "Bengaluru", "max": 132}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Chennai", "max": 128}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Delhi", "max": 148}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Hyderabad", "max": 116}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Kolkata", "max": 134}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Mumbai", "max": 130}, {"b2b_sales_medium": "Enterprise Sellers", "city": "Pune", "max": 114}, {"b2b_sales_medium": "Marketing", "city": "Bengaluru", "max": 138}, {"b2b_sales_medium": "Marketing", "city": "Chennai", "max": 104}, {"b2b_sales_medium": "Marketing", "city": "Delhi", "max": 137}, {"b2b_sales_medium": "Marketing", "city": "Hyderabad", "max": 121}, {"b2b_sales_medium": "Marketing", "city": "Kolkata", "max": 91}, {"b2b_sales_medium": "Marketing", "city": "Mumbai", "max": 92}, {"b2b_sales_medium": "Marketing", "city": "Pune", "max": 210}, {"b2b_sales_medium": "Online Leads", "city": "Bengaluru", "max": 75}, {"b2b_sales_medium": "Online Leads", "city": "Chennai", "max": 45}, {"b2b_sales_medium": "Online Leads", "city": "Delhi", "max": 91}, {"b2b_sales_medium": "Online Leads", "city": "Hyderabad", "max": 72}, {"b2b_sales_medium": "Online Leads", "city": "Kolkata", "max": 39}, {"b2b_sales_medium": "Online Leads", "city": "Mumbai", "max": 48}, {"b2b_sales_medium": "Online Leads", "city": "Pune", "max": 47}, {"b2b_sales_medium": "Partners", "city": "Bengaluru", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Chennai", "max": 83}, {"b2b_sales_medium": "Partners", "city": "Delhi", "max": 125}, {"b2b_sales_medium": "Partners", "city": "Hyderabad", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Kolkata", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Mumbai", "max": 91}, {"b2b_sales_medium": "Partners", "city": "Pune", "max": 90}, {"b2b_sales_medium": "Tele Sales", "city": "Bengaluru", "max": 85}, {"b2b_sales_medium": "Tele Sales", "city": "Chennai", "max": 40}, {"b2b_sales_medium": "Tele Sales", "city": "Delhi", "max": 91}, {"b2b_sales_medium": "Tele Sales", "city": "Hyderabad", "max": 70}, {"b2b_sales_medium": "Tele Sales", "city": "Kolkata", "max": 73}, {"b2b_sales_medium": "Tele Sales", "city": "Mumbai", "max": 85}, {"b2b_sales_medium": "Tele Sales", "city": "Pune", "max": 77}])



df = load_data()

st.subheader("Here's the data:")
st.dataframe(df)
st.subheader("Here's the chart:")
st.bar_chart(df, x='b2b_sales_medium', y='max')
st.subheader("And, the SQL was")
st.code(sql)
