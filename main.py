
import streamlit as st
import pandas as pd
import numpy as np
import json

st.title('Dashqueries: Analyzing Opportunities')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/RichaVerma/dashqueries-streamlit/blob/main/data.json')

def load_data():
    data = json.load(DATA_URL)
    return data

data = load_data()

st.write(data)
