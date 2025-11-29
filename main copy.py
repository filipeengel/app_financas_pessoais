import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel('database.xlsx')

# Preprocess data
df['month'] = df['Data'].apply(lambda x: str(x.year) + " - " + str(x.month))

# Streamlit
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")
st.title("Dashboard Finanças Pessoais")

month = st.sidebar.selectbox("Select Month", df['month'].unique())
df_despesas = df[df['month'] == month]
df_despesas = df_despesas[df_despesas['Rec/Des'] == 'Despesa']
df_despesas['Valor'] = df_despesas['Valor'].abs()

col1, col2 = st.columns(2)
col3 = st.columns(1)

fig_date = px.bar(df_despesas, x='Data', y='Valor',color='Categoria', title='Valor over Time')
col1.plotly_chart(fig_date, use_container_width=True)

fig_tipo = px.pie(df_despesas, values='Valor', names='Categoria', title='Distribution by Tipo')
col2.plotly_chart(fig_tipo, use_container_width=True)

fig_table = df_despesas[['Data', 'Categoria', 'Valor', 'Descrição']].sort_values(by='Data', ascending=True)
col3[0].dataframe(fig_table, use_container_width=True)