
import streamlit as st
import pandas as pd
import numpy as np


st.title('Dashqueries: Analyzing Opportunities')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/RichaVerma/dashqueries-streamlit/blob/main/data.json')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    print(data)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(100)

st.write(data)
