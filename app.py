import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sales Entry", layout="wide")

st.title('Sales Entry Page')

# data
sales_peeps = ['Barry', 'Paul', 'Cassandra']
data = pd.read_csv('C:/Users/User/Documents/Personal Projects/WebApp2/sales.csv')

# sections
col1 = st.sidebar

# data entry
col1.title('Enter New Sale')
account_exec = col1.text_input(label='Account Executive')
client = col1.text_input(label='Client')
sale_value = col1.number_input(label='Amount')

# display
if (account_exec in sales_peeps) and (client != "") and (sale_value > 0):
    st.markdown(f'Congratulations on your sale to {client}, {account_exec}! Your comission will be £{int(np.round((0.05*sale_value),0))}.')
else:
    st.write('Please enter valid details.')

if st.button(label='Add to Database', help='Only press once per sale'):
    data = data.append({'account_exec':account_exec, 'client':client, 'amount':sale_value, 'datetime':datetime.now()}, ignore_index=True)
    data.to_csv('C:/Users/User/Documents/Personal Projects/WebApp2/sales.csv', index=False)
    st.markdown('Your sale has been submitted to the database.')

# columns
col2, col3 = st.beta_columns([3, 2])
col2.dataframe(data)
grouped_data = data.groupby(['account_exec']).sum()
col3.bar_chart(grouped_data)